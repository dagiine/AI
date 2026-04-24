import pandas as pd
import numpy as np

df = pd.read_csv("loan_train.csv")
df["Status"] = df["Status"].map({"Y": "safe", "N": "risky"})

features = ["Married", "Dependents", "Education", "Self_Employed", "Applicant_Income", 
            "Coapplicant_Income", "Loan_Amount", "Term", "Credit_History", "Area"]
target = "Status"
numeric_features = ["Applicant_Income", "Coapplicant_Income", "Loan_Amount", "Term", "Credit_History"]
categorical_features = ["Married", "Dependents", "Education", "Self_Employed", "Area"]

# өгөгдөл цэвэрлэх
for col in numeric_features:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

for col in categorical_features:
    df[col] = df[col].fillna("Missing").astype(str)

df = df.dropna(subset=[target]).reset_index(drop=True)



# хамгийн олон давтагдсан утга
def majority(y):
    counts = {}

    for value in y:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    max_count = 0
    majority_class = None

    for key in counts:
        if counts[key] > max_count:
            max_count = counts[key]
            majority_class = key

    return majority_class

def classification_error(y):
    if len(y) == 0:
        return 0

    counts = {}

    for value in y:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    max_count = 0
    for key in counts:
        if counts[key] > max_count:
            max_count = counts[key]

    return 1 - max_count / len(y)

def weighted_error(groups):
    total = 0

    for g in groups:
        total += len(g)

    error = 0
    for g in groups:
        if len(g) > 0:
            weight = len(g) / total
            err = classification_error(g)
            error += weight * err

    return error


class Node:
    def __init__(self, prediction=None):
        self.prediction = prediction
        self.feature = None
        self.threshold = None
        self.children = {}
        self.is_numeric = False

    def is_leaf(self):
        return self.feature is None


def best_threshold_split(X_col, y):
    values = np.sort(np.unique(X_col))

    if len(values) <= 1:
        return None, float("inf"), None, None

    best_t, best_e = None, float("inf")
    best_l, best_r = None, None

    for i in range(len(values)-1):
        t = (values[i] + values[i+1]) / 2
        l_mask = X_col < t
        r_mask = X_col >= t

        e = weighted_error([y[l_mask], y[r_mask]])

        if e < best_e:
            best_t, best_e = t, e
            best_l, best_r = l_mask, r_mask

    return best_t, best_e, best_l, best_r


def best_categorical_split(X_col, y):
    groups = []
    masks = {}

    for val in X_col.unique():
        mask = X_col == val
        masks[val] = mask
        groups.append(y[mask])

    return weighted_error(groups), masks


def best_split(X, y):
    best_feature, best_groups = None, None
    best_threshold, best_error = None, float("inf")
    best_is_numeric = False

    for f in features:
        X_col = X[f]

        if f in numeric_features:
            t, e, l, r = best_threshold_split(X_col.values, y.values)
            if t is not None and e < best_error:
                best_feature = f
                best_threshold = t
                best_error = e
                best_groups = {"left": l, "right": r}
                best_is_numeric = True
        else:
            e, masks = best_categorical_split(X_col, y)
            if e < best_error:
                best_feature = f
                best_threshold = None
                best_error = e
                best_groups = masks
                best_is_numeric = False

    return best_feature, best_threshold, best_groups, best_is_numeric, best_error


def build_tree(X, y, depth=0, max_depth=5):
    node = Node(prediction=majority(y))

    # зогсох нөхцөл
    if len(set(y)) == 1 or depth >= max_depth:
        return node

    feature, threshold, groups, is_numeric, error = best_split(X, y)
    if feature is None:
        return node

    node.feature = feature
    node.threshold = threshold
    node.is_numeric = is_numeric

    if is_numeric:
        # empty шалгах
        if sum(groups["left"]) == 0 or sum(groups["right"]) == 0:
            return node

        node.children["left"] = build_tree(
            X[groups["left"]], y[groups["left"]], depth+1
        )
        node.children["right"] = build_tree(
            X[groups["right"]], y[groups["right"]], depth+1
        )

    else:
        for val, mask in groups.items():
            # empty шалгах
            if sum(mask) == 0:
                continue

            node.children[val] = build_tree(
                X[mask], y[mask], depth+1
            )

    return node


def print_tree(node, indent=""):
    if node.is_leaf():
        print(indent + "Prediction = " + node.prediction)
        return

    if node.is_numeric:
        print(indent + f"[{node.feature} < {node.threshold:.2f}]")
        print(indent + "  True:")
        print_tree(node.children["left"], indent + "    ")
        print(indent + "  False:")
        print_tree(node.children["right"], indent + "    ")
    else:
        print(indent + f"[{node.feature}]")
        for val, child in node.children.items():
            print(indent + f"  = {val}:")
            print_tree(child, indent + "    ")


# train
train = df.sample(frac=0.8, random_state=42)
test = df.drop(train.index)

tree = build_tree(train[features], train[target])

def predict(node, x):
    while node.is_leaf() == False:
        if node.is_numeric:
            if x[node.feature] < node.threshold:
                node = node.children["left"]  
            else:
                node = node.children["right"]  
        else:
            val = x[node.feature] 

            if val in node.children:
                node = node.children[val]
            else:
                return node.prediction  

    return node.prediction


correct = 0

for index, row in test.iterrows():
    x = row                      
    y_true = row[target]       

    y_pred = predict(tree, x)

    if y_pred == y_true:
        correct += 1

accuracy = correct / len(test)

print("Accuracy:", round(accuracy * 100, 2), "%")