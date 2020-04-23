import fnmatch
import io
import os
import sys
import time
import math

spam_cond = {}
ham_cond = {}
test_vocab = {}

def read_model(file):
    global spam_cond
    global ham_cond
    global test_vocab
    spam_prior = 0
    ham_prior = 0
    

    myfile = open(file, 'r')
    model_list = myfile.read().split("\t")

    test_vocab = eval(model_list[0])
    spam_prior = eval(model_list[1])
    ham_prior = eval(model_list[2])
    spam_cond = eval(model_list[3])
    ham_cond = eval(model_list[4])


# train_vocab, spam_prior, ham_prior, spam_cond, ham_cond = read_model('nbmodel.txt')
#take list of words and put them in the dictionary
def build_dict(dicti, words):
    temp = dicti

    for word in words:
        if word != '':
            if word in temp:
                temp[word] += 1
            else:
                temp[word] = 1
    return temp

#get the frequency of words stored in the dictionary
def get_size_dict(dicti):
    freq = 0
    for word in dicti:
        freq += dicti[word]
    return freq

# Reads a file and returns the words of the file split by space
def read_files(file):
    myfile = open(file, "r", encoding="latin1")
    content = myfile.read()
    content = content.lower()
    lines = content.splitlines()
    words = []
    for line in lines:
        words.append(line.split(" "))

    flat_words = [word for line in words for word in line]

    myfile.close()
    # print(flat_words)
    return flat_words

def NB_Classify(file):
    dict_of_file = {}
    spam_pred = 0
    ham_pred = 0

    dict_of_file = build_dict(dict_of_file, read_files(file))

    for word in dict_of_file:
        if word in spam_cond:
            # print(spam_cond[word])
            spam_pred += math.log(spam_cond[word])
        else:
            continue

    for word in dict_of_file:
        if word in ham_cond:
            
            ham_pred += math.log(ham_cond[word])
        else:
            continue

    return spam_pred, ham_pred

def write_output():
    myFile = open('nboutput.txt', "w")
    # op_string = ""
    t_path = sys.argv[1]
    files = []

    for root, d_names, f_names in os.walk(t_path):
        for f_name in fnmatch.filter(f_names, '*.txt'):
            f_name = os.path.join(root, f_name)
            files.append(f_name)
    
    for file in files:
        spam_pred, ham_pred = NB_Classify(file)
        # print(ham_pred)
        if spam_pred > ham_pred:
            op_string = "spam" + "\t" + file
         
        else:
            op_string = "ham" + "\t" + file

        myFile.write(op_string)
        myFile.write("\n")
    myFile.close()

if __name__ == "__main__":
    read_model('nbmodel.txt')
    # print(ham_cond)
    write_output()
    # print(NB_Classify('/Users/narry/Google Drive File Stream/My Drive/Academics/Spring 2020/NLP/Project1/Spam or Ham/dev/4/ham/0068.2000-01-18.beck.ham.txt'))


