__author__ = 'Wanchun Zhao'

import sqlite3
from Review import *
from Business import *
from Review_stats import *
from CommonPhrases import *

DATABASE_NAME = "reviews.db"

# print instructions
def print_instructions():
    return "Please choose an option:\n" \
           "1. Show the number of positive and negative reviews, the percentage of positive and negative reviews\n" \
           "2. Show the top n common phrases\n" \
           "3. Show the top n common phrases for positive reviews\n" \
           "4. Show the top n common phrases for negative reviews\n" \
           "5. Show examples of positive reviews\n" \
           "6. Show examples of negative reviews\n" \
           "7. Exit\n"


# show numbers of positive reviews, negative reviews and percentage
def option1_show_number_percentage(business_ids):

    # for each business_id, extract the number of positive and negative reviews, and sum them up
    for business_id in business_ids:
        review_stats=Review_stats(business_id.business_id,"","","","")
        review_stats=review_stats.get_number_of_reviews()

        # print the result
        print "For business_id",review_stats.business_id
        print "The number of positive reviews is: ",review_stats.number_of_positive_reviews
        print "The number of negative reviews is: ",review_stats.number_of_negative_reviews
        print "The percentage of positive reviews is: ", review_stats.percentage_of_positive_reviews
        print "The percentage of negative reviews is: ",review_stats.percentage_of_negative_reviews


# show the top n common phrases ordered by phrase frequency
def option2_top_n_common_phrases(business_ids):
    limit=int(input("Please enter the number of n: ")) # limit is the value of n
    for business_id in business_ids:
        common_phrases=list()
        common_phrase=CommonPhrases("",business_id.business_id,"","")
        common_phrases=common_phrase.get_common_phrases_by_business_id(limit)
        print "for business id:",business_id.business_id
        print "The top",limit,"common phrases are their frequencies are listed below:"
        for each_common_phrase in common_phrases:
            print each_common_phrase.common_phrase,each_common_phrase.frequency_of_phrase

# split review text into words, used in option 3 and 4
def split_text(review_text):
    list_of_words=list()
    review_text=review_text.rstrip()
    review_text=review_text.lower()
    review_text=review_text.replace(',','')
    review_text=review_text.replace('.','')
    review_text=review_text.replace('!','')
    review_text=review_text.replace('?','')
    words=review_text.split(' ')
    list_of_words.extend(words)
    return list_of_words

# construction of common phrases dictionary, used in option 3 and 4
def dictionary_construction(list_of_words,word_dictionary):
    for word in list_of_words:
        if word!=' ':
            if word not in word_dictionary:
                word_dictionary[word]=1
            else:
                word_dictionary[word]+=1
    return word_dictionary

#show top n common phrases for positive reviews
def option3_top_n_pos_common_phrases(business_ids):
    limit=int(input("Please enter the number of n: "))
    list_of_common_phrase=list()
    for business_id in business_ids:
        review = Review("", "", "", "", "", "", "", "", "", "")
        # geit all positive reviews for one business_id
        positive_reviews=review.get_all_reviews_by_business_id_and_sentiment(business_id.business_id,'pos')

        list_of_words=list()
        word_dictionary=dict()
        #split review text into a list of words
        for each_review in positive_reviews:
            words=split_text(each_review.text)
            list_of_words.extend(words)
        #construction of common phrases dictionary for positive reviews
        word_dictionary=dictionary_construction(list_of_words,word_dictionary)
        # sort the dictionary by value, turn it into a tuple
        sort_word_dictionary=sorted(word_dictionary.items(),key=lambda x:x[1],reverse=True)
        index=0
        # print result
        for word in sort_word_dictionary:
            if index>=limit:
                break
            print word[0],word[1]
            index+=1



# show top n common_phrases for negative reviews
def option4_top_n_neg_common_phrases(business_ids):
    limit=int(input("Please enter the number of n: "))
    list_of_common_phrase=list()
    for business_id in business_ids:
        review = Review("", "", "", "", "", "", "", "", "", "")
        negative_reviews = review.get_all_reviews_by_business_id_and_sentiment(business_id.business_id,'neg')
        list_of_words=list()
        word_dictionary=dict()
        for each_review in negative_reviews:
            words=split_text(each_review.text)
            list_of_words.extend(words)
        word_dictionary=dictionary_construction(list_of_words,word_dictionary)
        sort_word_dictionary=sorted(word_dictionary.items(),key=lambda x:x[1],reverse=True)
        index=0
        for word in sort_word_dictionary:
            if index>=limit:
                break
            print word[0],word[1]
            index+=1


# show the examples of positive reviews
def option5_pos_examples(business_ids):

    for business_id in business_ids:
        review = Review("", "", "", "", "", "", "", "", "", "")
        positive_reviews = review.get_reviews_by_business_id_and_sentiment(business_id.business_id,'pos',5)
    index=1
    for positive_review in positive_reviews:
        print str(index)+".",positive_review.text.rstrip() # adjust the format
        index+=1


# show the examples of negative reviews
def option6_neg_examples(business_ids):

    for business_id in business_ids:
        review = Review("", "", "", "", "", "", "", "", "", "")
        negative_reviews = review.get_reviews_by_business_id_and_sentiment(business_id.business_id,'neg',5)
    index=1
    for negative_review in negative_reviews:
        print str(index)+".",negative_review.text.rstrip()
        index+=1





# main function
# Prompt user to retrieve reviews
def main():
    business_name = raw_input("Please enter a business name: ")
    option = raw_input(print_instructions())

    # get all business_ids
    business = Business("","","","","","","","","","","")
    business.name=business_name
    business_ids = business.get_ids_by_business_name()

    while option != '7':
        if option=='1':
            option1_show_number_percentage(business_ids)
        elif option=='2':
            option2_top_n_common_phrases(business_ids)
        elif option=='3':
            option3_top_n_pos_common_phrases(business_ids)
        elif option=='4':
            option4_top_n_neg_common_phrases(business_ids)
        elif option == '5':
            option5_pos_examples(business_ids)
        elif option=='6':
            option6_neg_examples(business_ids)


        print ""
        option = raw_input(print_instructions())


main()












