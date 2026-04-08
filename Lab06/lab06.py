import random

def load_data(filename):
    data = [] 
    file = open(filename, "r")   

    next(file) #ehnii mur algasah

    for line in file:
        if line.strip() == "": 
            continue 

        parts = line.strip().split(",")
        x1 = float(parts[1])  
        x2 = float(parts[2])  
        x3 = float(parts[3])  
        x4 = float(parts[4])  
        features = [x1, x2, x3, x4] 

        label_text = parts[5]
        if label_text == "Iris-setosa":  
            label = 0   # setosa = 0
        elif label_text == "Iris-versicolor":  
            label = 1   # versicolor = 1
        else:  
            label = 2   # virginica = 2

        data.append((features, label)) 

    file.close()  
    return data 

def split_data(data): 
    random.shuffle(data)

    total = len(data)  
    train_size = int(total * 0.7) 

    train_data = []  
    test_data = [] 

    for i in range(train_size):  
        train_data.append(data[i])  

    for i in range(train_size, total):  
        test_data.append(data[i])  

    return train_data, test_data  

class Perceptron:  
    def __init__(self):  
        self.learning_rate = 0.1
        self.weights = []  

        for c in range(3):  
            w = [] 
            for i in range(5):  
                w.append(random.uniform(-1, 1))  
            self.weights.append(w)  

    def add_bias(self, x):  
        new_ft = []  
        for value in x: 
            new_ft.append(value)  
        new_ft.append(1)  

        return new_ft 

    def predict(self, x):  
        x = self.add_bias(x)  
        scores = [] 

        for w in self.weights:  
            score = 0  
            for i in range(len(x)):  
                score = score + w[i] * x[i]  
            scores.append(score)  
 
        return max(range(len(scores)), key=lambda i: scores[i])

    def training(self, train_data): 
        epochs = 20 

        for e in range(epochs): 
            for item in train_data: 
                features = item[0] 
                true_label = item[1] 

                predicted = self.predict(features) 
                x = self.add_bias(features) 

                for i in range(len(x)): 
                    self.weights[true_label][i] += ( 
                        self.learning_rate * x[i] 
                    ) 
                    self.weights[predicted][i] -= ( 
                        self.learning_rate * x[i] 
                    )

def test_model(model, test_data):  
    correct = 0 

    for item in test_data:  
        features = item[0]  
        true_label = item[1]  

        predicted = model.predict(features) 
        if predicted == true_label: 
            correct += 1 
        print("Predicted:", predicted, "True:", true_label)
    
    accuracy = correct / len(test_data)  

    print("\nTotal test samples:", len(test_data))
    print("Correct predictions:", correct)
    print("Test Accuracy:", accuracy * 100, "%")

# main
data = load_data("iris.csv")
train_data, test_data = split_data(data)

model = Perceptron()
model.training(train_data)

test_model(model, test_data)