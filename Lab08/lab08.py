import os    
import math   

# Хавтаснаас suffix тохирох бүх файлыг уншина
# TRAIN_SPAM_SUFFIX = ".GP.spam.txt"
# TRAIN_HAM_SUFFIX  = ".farmer.ham.txt"
# DEV_SPAM_SUFFIX   = ".GP.spam.txt"
# DEV_HAM_SUFFIX    = ".farmer.ham.txt"

def load_emails(folder_path, suffix):
    emails = []                              
    file_list = os.listdir(folder_path)     

    i = 0
    while i < len(file_list):               
        file_name = file_list[i]             
        if file_name.endswith(suffix):       # Хэрэв suffix таарч байвал
            full_path = os.path.join(folder_path, file_name)  # Хавтасны нэр болон файлын нэрийг нийлүүлж бүтэн зам үүсгэнэ.

            file = open(full_path, "r", encoding="latin-1")  
            text = file.read()               
            file.close()                    

            emails.append(text.lower().split())  

        i = i + 1

    return emails


# Бүх захиадаас ялгаатай үгсийг цуглуулж vocabulary үүсгэнэ
def build_vocabulary(all_emails):
    vocabulary = {}                         

    i = 0
    while i < len(all_emails):
        words = all_emails[i]               
        j = 0
        while j < len(words):
            word = words[j]
            if word not in vocabulary:
                vocabulary[word] = len(vocabulary)  
            j = j + 1
        i = i + 1

    return vocabulary

def count_words(words):
    word_counts = {}
 
    i = 0
    while i < len(words):
        word = words[i]
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
        i = i + 1
 
    return word_counts

# unigram өгөгдөл бэлдэнэ
def bag_of_words(words, vocabulary):
    row = []

    k = 0
    while k < len(vocabulary):
        row.append(0)
        k = k + 1

    # Үг бүр хэд давтагдсаныг тоолох
    word_counts = count_words(words)

    # Тоолсон утгуудыг row-д байрлуулах
    word_list = list(word_counts.keys())
    i = 0
    while i < len(word_list):
        word = word_list[i]
        if word in vocabulary:             
            id = vocabulary[word]         
            row[id] = word_counts[word]   
        i = i + 1

    return row


# Бүх email-ийг матриц болгоно
def build_bow_matrix(emails, vocabulary):
    matrix = []

    i = 0
    while i < len(emails):
        row = bag_of_words(emails[i], vocabulary)  
        matrix.append(row)                       
        i = i + 1

    return matrix

# Matrix-ын бүх нүдийн нийлбэр (нийт үгийн тоо)
def sum_matrix(matrix):
    total = 0
 
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            total = total + matrix[i][j]
            j = j + 1
        i = i + 1
 
    return total
 
 
# Matrix-ын баганын нийлбэр (тухайн үг нийт хэдэн удаа орсон)
def sum_columns(matrix, n_vocab):
    column_sums = []
 
    j = 0
    while j < n_vocab:
        column_sums.append(0)
        j = j + 1
 
    i = 0
    while i < len(matrix):
        j = 0
        while j < n_vocab:
            column_sums[j] = column_sums[j] + matrix[i][j]
            j = j + 1
        i = i + 1
 
    return column_sums

# P(spam | w1, w2, .. wN) = P(spam)*П P(Wi | spam)
# P(ham | w1, w2, ... wN) = P(ham)* П P(wi | ham)
def train_naive_bayes(spam_matrix, ham_matrix, n_vocab, alpha=1):
    n_spam = len(spam_matrix)
    n_ham = len(ham_matrix)
    p_spam = n_spam / (n_spam + n_ham)
    p_ham = n_ham  / (n_spam + n_ham) 

    # Spam/ham email-үүд доторх нийт үгийн тоо
    n_spam_words = sum_matrix(spam_matrix)
    n_ham_words  = sum_matrix(ham_matrix)

    # Үг бүр spam-д хэд, ham-д хэд давтагдсан
    n_wi_spam = sum_columns(spam_matrix, n_vocab)
    n_wi_ham  = sum_columns(ham_matrix,  n_vocab)

    log_p_wi_spam = []
    log_p_wi_ham  = []

    # Тухайн үг spam/ham ангилалд байх магадлал
    j = 0
    while j < n_vocab:
        prob_spam = (n_wi_spam[j] + alpha) / (n_spam_words + alpha * n_vocab)
        prob_ham  = (n_wi_ham[j]  + alpha) / (n_ham_words  + alpha * n_vocab)

        log_p_wi_spam.append(math.log(prob_spam))
        log_p_wi_ham.append(math.log(prob_ham))

        j = j + 1

    model = {"p_spam": p_spam, "p_ham": p_ham, "log_p_wi_spam": log_p_wi_spam, "log_p_wi_ham": log_p_wi_ham}

    return model


# email-ийг ангилах
def classify(email_words, vocabulary, model):
    log_prob_spam = math.log(model["p_spam"])
    log_prob_ham  = math.log(model["p_ham"])

    word_counts = count_words(email_words)

    # Тухайн үг spam/ham байх магадлал
    word_list = list(word_counts.keys())
    i = 0
    while i < len(word_list):
        word = word_list[i]
        if word in vocabulary:
            id = vocabulary[word]
            count = word_counts[word]

            log_prob_spam += count * model["log_p_wi_spam"][id]
            log_prob_ham  += count * model["log_p_wi_ham"][id]
        i = i + 1

    # Аль нь их байгаагаар нь шийднэ
    if log_prob_spam >= log_prob_ham:
        return "spam"
    else:
        return "ham"


# Accuracy тооцох
def evaluate(dev_emails, dev_labels, vocabulary, model):
    correct = 0
    total = len(dev_emails)

    spam_correct = 0
    spam_wrong   = 0
    ham_correct  = 0
    ham_wrong    = 0

    i = 0
    while i < total:
        prediction = classify(dev_emails[i], vocabulary, model)
        actual = dev_labels[i]

        if prediction == actual:
            correct += 1

            if actual == "spam":
                spam_correct += 1
            else:
                ham_correct += 1

        else:
            if actual == "spam":
                spam_wrong += 1
            else:
                ham_wrong += 1

        i += 1

    accuracy = correct / total

    return accuracy, correct, total, spam_correct, spam_wrong, ham_correct, ham_wrong

if __name__ == "__main__":

    TRAIN_SPAM_FOLDER = "train/spam"
    TRAIN_HAM_FOLDER  = "train/ham"
    DEV_SPAM_FOLDER   = "dev/spam"
    DEV_HAM_FOLDER    = "dev/ham"

    TRAIN_SPAM_SUFFIX = ".GP.spam.txt"
    TRAIN_HAM_SUFFIX  = ".farmer.ham.txt"
    DEV_SPAM_SUFFIX   = ".GP.spam.txt"
    DEV_HAM_SUFFIX    = ".farmer.ham.txt"

    train_spam = load_emails(TRAIN_SPAM_FOLDER, TRAIN_SPAM_SUFFIX)
    train_ham  = load_emails(TRAIN_HAM_FOLDER,  TRAIN_HAM_SUFFIX)
    print("Training spam:", len(train_spam)) 
    print("Training ham: ", len(train_ham))

    vocabulary = build_vocabulary(train_spam + train_ham)
    n_vocab = len(vocabulary)
    print("\nНийт ялгаатай үгийн тоо (N_vocab):", n_vocab)

    spam_bow_matrix = build_bow_matrix(train_spam, vocabulary)
    ham_bow_matrix  = build_bow_matrix(train_ham,  vocabulary)
    print("\nBag of Words матриц")
    print("Spam:", len(spam_bow_matrix), "x", n_vocab)
    print("Ham: ", len(ham_bow_matrix),  "x", n_vocab)

    model = train_naive_bayes(spam_bow_matrix, ham_bow_matrix, n_vocab, alpha=1)
    print("\nP(spam) =", round(model["p_spam"], 4))
    print("P(ham)  =", round(model["p_ham"],  4))

    dev_spam = load_emails(DEV_SPAM_FOLDER, DEV_SPAM_SUFFIX)
    dev_ham  = load_emails(DEV_HAM_FOLDER,  DEV_HAM_SUFFIX)

    dev_emails = dev_spam + dev_ham
    dev_labels = []

    i = 0
    while i < len(dev_spam):
        dev_labels.append("spam")
        i = i + 1

    i = 0
    while i < len(dev_ham):
        dev_labels.append("ham")
        i = i + 1

    accuracy, correct, total, sc, sw, hc, hw = evaluate(dev_emails, dev_labels, vocabulary, model)

    print("\nAll emails:", total)
    print("Correct:", correct)
    print("Accuracy: {:.2f}%".format(accuracy * 100))

    print("\nSpam зөв:", sc)
    print("Spam буруу:", sw)
    print("\nHam зөв:", hc)
    print("Ham буруу:", hw)