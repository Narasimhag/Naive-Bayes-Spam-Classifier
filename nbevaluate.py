import io
import sys

def read_output(file):
    spam_correct_counter = 0
    ham_correct_counter = 0
    spam_incorrect_counter = 0
    ham_incorrect_counter = 0
    spam_counter = 0
    ham_counter = 0
    myFile = open(file, "r")
    
   
    for line in myFile:
        
        label_path = line.split("\t")
        cat = label_path[1].split('/')[-2]
        # print(cat, label_path[0])

        if cat == 'spam':
            if label_path[0] == 'spam':
                spam_correct_counter += 1
            elif label_path[0] == 'ham':
                ham_incorrect_counter += 1
            else:
                print('a')

            # print('inspam')
            spam_counter += 1

        elif cat == 'ham':
            if label_path[0] == 'ham':
                ham_correct_counter += 1
            elif label_path[0] == 'spam':
                spam_incorrect_counter += 1
            else:
                print('w')

            ham_counter += 1    
    
    # print(spam_correct_counter, spam_counter, spam_incorrect_counter)
    # print(ham_correct_counter, ham_counter, ham_incorrect_counter)
    spam_recall = spam_correct_counter/spam_counter
    ham_recall = ham_correct_counter/ham_counter

    spam_precision = spam_correct_counter/(spam_correct_counter + spam_incorrect_counter)
    ham_precision = ham_correct_counter / (ham_correct_counter + ham_incorrect_counter)

    spam_fscore = (2 * spam_precision * spam_recall) / (spam_precision + spam_recall)
    ham_fscore = (2* ham_precision * ham_recall) / (ham_precision + ham_recall)

    print(spam_precision, spam_recall, spam_fscore, ham_precision, ham_recall, ham_fscore)

if __name__ == "__main__":
    fileName = sys.argv[1]
    read_output(fileName)

