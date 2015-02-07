__author__ = 'Wanchun Zhao'

import sqlite3

TABLE_NAME = "sentiment"
DATABASE_NAME = "reviews.db"
COLUMN_REVIEW_ID = "review_id"
COLUMN_BUSINESS_ID = "business_id"
COLUMN_SENTIMENT = "sentiment"



class Sentiment:
    # constructor
    def __init__(self, review_id, business_id, sentiment):
        self.review_id=review_id
        self.business_id=business_id
        self.sentiment=sentiment

    # insert data into sentiment table
    def insert(self):
        conn=sqlite3.connect(DATABASE_NAME)
        conn.execute("INSERT INTO {0} ({1},{2},{3}) VALUES (?,?,?);".
                     format(TABLE_NAME, COLUMN_REVIEW_ID, COLUMN_BUSINESS_ID,COLUMN_SENTIMENT),
                     (self.review_id, self.business_id, self.sentiment))
        conn.commit()
        conn.close()


