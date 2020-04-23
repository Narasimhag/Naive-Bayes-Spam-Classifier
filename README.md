# Naive-Bayes-Spam-Classifier

## Description

Email spam classification is a classic application of NLP. While we are not wrong to think that some ML magic happens here,
the classifier uses a technique from probability theory, [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier). This project implements the Naive Bayes classifier in Python.  

### Built With
* [Python 3](https://www.python.org/downloads/)
* [Some knowledge on Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)
* [Data to train on!](https://drive.google.com/file/d/191Sjgex29INyKPBJ5hoBoUWO9JivB3hr/view?usp=sharing)

## Getting Started

To get a local copy up and running follow these simple example steps.

### Pre-requisites
* Install Python. Detailed instructions for installation can be found [here](https://realpython.com/installing-python/). 
* Mac users, with homebrew can run the following command in their terminal.
```sh
brew install python3
```
* While I can give the command for conda users to install python, if you're running conda, you'd probably have it. You can check the version to make sure it is Python 3.
```sh
python --version
```
### Installation
* Clone this project using the following command.
```sh
git clone https://github.com/Narasimhag/Naive-Bayes-Spam-Classifier.git
```

### Usage

1. Download the data from the link above and extract it to the project directory, created after running the clone command, typically named 'Naive-Bayes-Spam-Classifier'.
2. Train the model, by running nbtrain.py.
```sh
python3 nblearn.py /path/to/folder/train
```
3. The file nbmodel.txt would update with the model.
4. To classify, run nbclassify.py
```sh
python3 nbclassify.py /path/to/folder/dev
```
5. You can also try it on your own test data by giving nbclassify the path to folder.
6. The labels will be populated in nboutput.py
7. Running nbevaluate.py will give the precision, recall and f-score of the model, which in my case was around 99.1%, 99.5 and 99.3% for spam; 98.7%, 97.8% and 98.2% for ham emails.


## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Contact
If you have some criticism or want to say some nice things about the project, please feel free to tweet me. [@raogundavarapu](www.twitter.com/raogundavarapu) or email me at raonarasimha050@gmail.com
