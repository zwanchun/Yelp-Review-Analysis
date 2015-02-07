__author__ = 'Wanchun Zhao'

import sqlite3

DATABASE_NAME = "reviews.db"
TABLE_NAME = "common_phrases"
COLUMN_BUSINESS_ID="business_id"
COLUMN_COMMON_PHRASE="common_phrase"
COLUMN_FREQUENCY_OF_PHRASE="frequency_of_phrase"

class CommonPhrases:
    # constructor
    def __init__(self,phrase_id,business_id,common_phrase,frequency_of_phrase):
        self.phrase_id=phrase_id
        self.business_id=business_id
        self.common_phrase=common_phrase
        self.frequency_of_phrase=frequency_of_phrase

    # insert data into common_phrases table
    def insert(self,word_dictionary):
        conn=sqlite3.connect(DATABASE_NAME)

        for key in word_dictionary:
            conn.execute("INSERT INTO {0} ({1},{2},{3}) VALUES (?,?,?);".
                     format(TABLE_NAME, COLUMN_BUSINESS_ID, COLUMN_COMMON_PHRASE,COLUMN_FREQUENCY_OF_PHRASE),
                     (self.business_id, key,word_dictionary[key]))

        conn.commit()
        conn.close()

    # Using business_id to get common_phrase and the frequency_of_phrase, ordered by frequency in descending order
    def get_common_phrases_by_business_id(self,limit):
        common_phrases=list()
        conn=sqlite3.connect(DATABASE_NAME)
        sql="select common_phrase,frequency_of_phrase from common_phrases where business_id='{0}' order by " \
            "frequency_of_phrase DESC limit {1}".format(self.business_id,limit)
        Rows=conn.execute(sql)
        for Row in Rows:
            common_phrase=CommonPhrases("","",Row[0],Row[1])
            common_phrases.append(common_phrase)

        return common_phrases
        conn.commit()
        conn.close()








