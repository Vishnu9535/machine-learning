import nltk
import random 
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
word={}
def features_extract(words):
    for x in words:
        word[x] = True
    return word

document = []
for cat in movie_reviews.categories():
    for fid in movie_reviews.fileids(cat):
        temp = list(movie_reviews.words(fid))
        tupe= (temp,cat)
        document.append(tupe)


featuresets = [(features_extract(words), category) for (words, category) in document]

train_set, test_set = featuresets[100:], featuresets[:100]
classifier = SklearnClassifier(MultinomialNB())
classifier.train(train_set)

print("Accuracy:", nltk.classify.accuracy(classifier, test_set))
input_sentence = input("Enter a sentence: ")
words = word_tokenize(input_sentence) 
features =features_extract(words)
print("Predicted sentiment:", classifier.classify(features))