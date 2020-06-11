import nltk
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
from pymystem3 import Mystem
from string import punctuation
import pickle

# Для первого запуска
# pip install nltk==3.3
# import nltk
# nltk.download('averaged_perceptron_tagger_ru')
# nltk.download('punkt')
# nltk.download('stopwords')
# pip3 install pymystem3
# pip install pandas
# pip install pandaspymystem3==0.1.10

import re, string, random

def lemmatize_sentence(text):
    mysteam = Mystem()
    tokens = mysteam.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in stop_words
              and token != " "
              and token.strip() not in punctuation]
    return tokens


# +
def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

#+
def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

#+
def tokenizer(tweets):
    tweets_tokens = []
    for tweet in tweets:
        tweets_tokens.append(nltk.word_tokenize(tweet))
    return tweets_tokens

if __name__ == "__main__":

    # Считываем данные
    n = ['id', 'date', 'name', 'text', 'typr', 'rep', 'rtw', 'faw', 'stcount', 'foll', 'frien', 'listcount']
    positive_tweets = pd.read_csv('C:/Users/Usvel/Desktop/untitled/positive.csv', sep=';', error_bad_lines=False, names=n, usecols=['text'])[:100]
    negative_tweets = pd.read_csv('C:/Users/Usvel/Desktop/untitled/negative.csv', sep=';', error_bad_lines=False, names=n, usecols=['text'])[:100]


    stop_words = stopwords.words('russian')

    positive_tweet_tokens = tokenizer(negative_tweets.text);
    negative_tweet_tokens = tokenizer(negative_tweets.text);

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    for tokens in positive_tweets.text:
        positive_cleaned_tokens_list.append(lemmatize_sentence(tokens))

    for tokens in negative_tweets.text:
        negative_cleaned_tokens_list.append(lemmatize_sentence(tokens))


    all_pos_words = get_all_words(positive_cleaned_tokens_list)

    freq_dist_pos = FreqDist(all_pos_words)
    print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    train_data = dataset[:7000]
    test_data = dataset[7000:]

    classifier = NaiveBayesClassifier.train(train_data)

    print("Accuracy is:", classify.accuracy(classifier, test_data))

    print(classifier.show_most_informative_features(10))

    custom_tweet = "Замечательный телефон, пользуюсь им уже 2 года, очень нравится"

    custom_tokens = lemmatize_sentence(custom_tweet)

    # # now you can save it to a file
    # joblib.dump(classify, 'filename.pkl')
    # # and later you can load it
    # classifier1 = joblib.load('filename.pkl')
    # now you can save it to a file with
    with open('filename.pkl', 'wb') as f: pickle.dump(classifier, f)
    # and later you can load it with
    with open('filename.pkl', 'rb') as f:
        clf = pickle.load(f)

    print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
    print(custom_tweet, clf.classify(dict([token, True] for token in custom_tokens)))


