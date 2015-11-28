import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.stem.porter import *


def read_tweets(file, clas):
  print 'reding data form file'
  print file
  f = open(file, 'r')
  words = []
  line = f.readline()
  while line!='':
    words.append((tokenize_sentance(line),clas))
    line = f.readline()
  print 'print reading dat from file completed'
  return words


def tokenize_sentance(line):
  stop = stopwords.words('english')
  stemmer = PorterStemmer()
  tokenizer = RegexpTokenizer(r'\w+')
  #words = [word.lower() for word in line.split() if word not in stop]
  #words = [word.lower() for word in nltk.word_tokenize(line) if word not in stop]
  words = [stemmer.stem(word) for word in tokenizer.tokenize(line) if word not in stop]
  return words

def train():
  positive_tweets = read_tweets('/root/295/new/positive.txt', 'positive')
  negative_tweets = read_tweets('/root/295/new/negative.txt', 'negative')
  print len(positive_tweets)
  print len(negative_tweets)

  #pos_train = positive_tweets[:2000]
  #neg_train = negative_tweets[:2000]
  #pos_test = positive_tweets[2001:3000]
  #neg_test = negative_tweets[2001:3000]
  pos_train = positive_tweets[:len(positive_tweets)*80/100]
  neg_train = negative_tweets[:len(negative_tweets)*80/100]
  pos_test = positive_tweets[len(positive_tweets)*80/100+1:]
  neg_test = negative_tweets[len(positive_tweets)*80/100+1:]

  training_data = pos_train + neg_train
  test_data = pos_test + neg_test

  sentim_analyzer = SentimentAnalyzer()
  all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_data])
  #print all_words_neg
  unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
  #print unigram_feats
  print len(unigram_feats)
  sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
  training_set = sentim_analyzer.apply_features(training_data)
  test_set = sentim_analyzer.apply_features(test_data)
  print test_set  
  trainer = NaiveBayesClassifier.train
  classifier = sentim_analyzer.train(trainer, training_set)
  for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))
  print sentim_analyzer.classify(tokenize_sentance('I hate driving car at night'))
  
  return sentim_analyzer


classifier = train()

def classify(input):
  return classifier.classify(tokenize_sentance(input))
