__author__ = 'Wanchun Zhao' \

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

from Sentiment import *
from Review import *
from Review_stats import *
from Business import *
from CommonPhrases import *

SENTIMENT_TYPE = 0

# This file constructs the whole database, including three tables: sentiment, review_stats and common_phrases

# split the text into words, used in the construction of common_phrases table
def split_text(review_text):
    list_of_words=list()
    # manipulation of text
    review_text=review_text.rstrip()
    review_text=review_text.lower()
    review_text=review_text.replace(',','')
    review_text=review_text.replace('.','')
    review_text=review_text.replace('!','')
    review_text=review_text.replace('?','')
    # split the words
    words=review_text.split(' ')
    # store all the words in a list
    list_of_words.extend(words)
    return list_of_words

# construct dictionary using common_phrases and corresponding frequency, used in construction of common_phrases table
def dictionary_construction(list_of_words,word_dictionary):
    for word in list_of_words:
        if word not in word_dictionary:
            word_dictionary[word]=1
        else:
            word_dictionary[word]+=1
    return word_dictionary

# insert dictionary items into common_phrases table
def insert_words(business_id,Reviews,word_dictionary):
    words = list()
    list_of_words = list()
    word_dictionary = dict()
    for each_review in Reviews:
        words = split_text(each_review.text)# split each review into words
        list_of_words.extend(words)#store all the words appeared in one business_id as a list
    word_dictionary = dictionary_construction(list_of_words, word_dictionary)# construction of common_phrase dictionary
    common_phrase = CommonPhrases("",business_id,"","")
    common_phrase.insert(word_dictionary)


def main():
    review = Review("", "", "","","","","","","","") # this will call your constructor
    # get 50 results from databases
    reviews = review.get_reviews("50")
    for a_review in reviews:
        #construction of sentiment table
        blob = TextBlob(a_review.text, analyzer=NaiveBayesAnalyzer())
        text_sentiment = blob.sentiment

        text_sentiment = text_sentiment[SENTIMENT_TYPE] #text_sentiment will either be pos (for positive) or neg (for negative)
        #here is where we create a Sentiment object
        sentiment = Sentiment(a_review.review_id, a_review.business_id, text_sentiment)
        sentiment.insert() #this will insert information into the sentiment table

    #construction of review_stats table
    review_stats=Review_stats("", "", "","","")
    review_stats.insert()#insert positive and negative reviews' information to review_stats table

    #construction of common_phrases table
    business=Business("","","","","","","","","","","")
    business_ids=business.get_all_business_ids()#acquire all business_ids from sentiment table
    Reviews=list()
    words=list()
    list_of_words=list()
    word_dictionary=dict()
    for business_id in business_ids:
        review=Review("","","","","","",business_id.business_id,"","","")
        Reviews=review.get_reviews_by_business_id()# get all reviews by business_id
        insert_words(business_id.business_id,Reviews,word_dictionary)# insert data into common_phrases table


main()

