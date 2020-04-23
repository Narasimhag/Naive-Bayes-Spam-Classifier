import sys
import os
import fnmatch
import io
import time


files = []
vocab = {}
spam = {}
ham = {}
spam_count = 0
ham_count = 0
stop_words = ['a', 'able', 'about', 'above', 'across', 'again', "ain't", 'all', 'almost', 'along', 'also', 'am', 'among', 'amongst', 'an', 'and', 'anyhow', 'anyone', 'anyway', 'anyways', 'appear', 'are', 'around', 'as', "a's", 'aside', 'ask', 'asking', 'at', 'away', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'behind', 'below', 'beside', 'besides', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'come', 'comes', 'consider', 'considering', 'corresponding', 'could', 'do', 'does', 'doing', 'done', 'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'either', 'else', 'elsewhere', 'etc', 'even', 'ever', 'every', 'ex', 'few', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'happens', 'has', 'have', 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him', 'himself', 'his', 'how', 'hows', 'i', "i'd", 'ie', 'if', "i'll", "i'm", 'in', 'inc', 'indeed', 'into', 'inward', 'is', 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'lately', 'later', 'latter', 'latterly', 'lest', 'let', "let's", 'looking', 'looks', 'ltd', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'might', 'most', 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'need', 'needs', 'neither', 'next', 'nine', 'no', 'non', 'now', 'nowhere', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'per', 'placed', 'que', 'quite', 're', 'regarding', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'seven', 'several', 'she', "she'd", "she'll", "she's", 'since', 'six', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'tell', 'tends', 'th', 'than', 'that', 'thats', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'theres', "there's", 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'think', 'third', 'this', 'those', 'though', 'three', 'through', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', "t's", 'twice', 'two', 'un', 'under', 'up', 'upon', 'us', 'use', 'used', 'uses', 'using', 'usually', 'value', 'various', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", "we'll", 'went', 'were', "we're", "weren't", "we've", 'what', 'whatever', "what's", 'when', 'whence', 'whenever', "when's", 'where', 'whereafter', 'whereas', 'whereby', 'wherein', "where's", 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', "who's", 'whose', 'why', "why's", 'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves', "you've"]
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

def removeStops(tokenList):
        output = []
        # loop through each token to see if it is in the drop list
        for token in tokenList:
            if token in stop_words:
                # do nothing
                continue
            else:
                # return token not in stopWords
                output.append(token)
        return output


# Naive Bayes - Step 1: Separate By class
def separate_by_class():
    global files
    global spam
    global ham
    global vocab
    global spam_count
    global ham_count
    
    dpath = sys.argv[1]
    # print(dpath)
    # start = time.time()
    for root, d_names, f_names in os.walk(dpath):
        for f_name in fnmatch.filter(f_names, '*.txt'):
            f_name = os.path.join(root, f_name)
            files.append(f_name)
        
    for file in files:
        path = file.split("/")
        if (path[-2] == 'spam'):
            spam = build_dict(spam, removeStops(read_files(file)))
            spam_count += 1
            vocab = build_dict(vocab, removeStops(read_files(file)))
        if (path[-2] == 'ham'):
            ham = build_dict(ham, removeStops(read_files(file)))
            ham_count += 1
            vocab = build_dict(vocab, removeStops(read_files(file)))

#Step 2 - Calculate prior and conditional probabilities

def train_NB():

    #prior_probabilities
    total_docs = len(files)
    spam_prob = spam_count / total_docs
    ham_prob = ham_count / total_docs

    #occurence of words in each class
    word_count_spam = {}
    word_count_ham = {}
    
    for word in vocab:
        if word in spam:
            word_count_spam[word] = spam[word]
        else:
            word_count_spam[word] = 0
    for word in vocab:
        if word in ham:
            word_count_ham[word] = ham[word]
        else:
            word_count_ham[word] = 0

    #conditional probabilities
    cond_prob_spam = {}
    cond_prob_ham = {}
    len_vocab = len(vocab)
    size_vocab = get_size_dict(vocab)
    size_word_count_spam = get_size_dict(word_count_spam)
    size_word_count_ham = get_size_dict(word_count_ham)

    for word in vocab:
        cond_prob_spam[word] = (word_count_spam[word] + 1) / (len_vocab + size_word_count_spam)
        cond_prob_ham[word] = (word_count_ham[word] + 1) / (len_vocab + size_word_count_ham)
    
    return spam_prob, ham_prob, cond_prob_spam, cond_prob_ham

# Step 3 - Write to nbmodel.txt

def write_model(file):
    myfile = open(file, 'w')

    spam_prior, ham_prior, spam_cond, ham_cond = train_NB()

    # print(spam_cond)
    myfile.write(str(vocab))
    myfile.write("\t")
    # myfile.write("******VOCAB END******")
    myfile.write(str(spam_prior))
    myfile.write("\t")
    # myfile.write("******SPAM PRIOR END******")
    myfile.write(str(ham_prior))
    myfile.write("\t")
    # myfile.write("******HAM PRIOR END******")
    myfile.write(str(spam_cond))
    myfile.write("\t")
    # myfile.write("******SPAM COND END******")
    myfile.write(str(ham_cond))
    # myfile.write("END")
    myfile.close()
    


    



            
    # print(files)
    # end = time.time()

    # print(end - start) #1.001, 0.9803, 0.8729 #np 0.4453, 0.5217, 0.4307

    # match = dpath + "/**/*.txt"
    # # o = glob.iglob(match, recursive=True)
    # # print(o)
    # # print(next(o))

    # files = glob.glob(match, recursive=True)
    # # print(files)
    # end = time.time()

    # print(end - start) #1.002, 1.2996, 1.3051 #np 0.6375, 0.6078, 0.5871





if __name__ == "__main__":
    # start = time.time()
    separate_by_class()
    write_model('nbmodel.txt')
    # end = time.time()

    # print(end - start)
   
    