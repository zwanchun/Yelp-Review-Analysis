__author__ = 'Wanchun Zhao'

import sqlite3

TABLE1_NAME = "sentiment"
TABLE2_NAME="review_stats"
DATABASE_NAME = "reviews.db"
COLUMN_BUSINESS_ID = "business_id"
COLUMN_NUMBER_OF_POSITIVE_REVIEWS = "number_of_positive_reviews"
COLUMN_NUMBER_OF_NEGATIVE_REVIEWS= "number_of_negative_reviews"
COLUMN_PERCENTAGE_OF_POSITIVE_REVIEWS="percentage_of_positive_reviews"
COLUMN_PERCENTAGE_OF_NEGATIVE_REVIEWS="percentage_of_negative_reviews"



class Review_stats:
    def __init__(self, business_id, number_of_positive_reviews, number_of_negative_reviews, percentage_of_positive_reviews,percentage_of_negative_reviews):
        self.business_id=business_id
        self.number_of_positive_reviews=number_of_positive_reviews
        self.number_of_negative_reviews=number_of_negative_reviews
        self.percentage_of_positive_reviews=percentage_of_positive_reviews
        self.percentage_of_negative_reviews=percentage_of_negative_reviews

    # insert data into database
    def insert(self):
        conn=sqlite3.connect(DATABASE_NAME)
        cur=conn.cursor()
        sql="SELECT distinct business_id From "+TABLE1_NAME
        cur.execute(sql)
        business_ids=cur.fetchall()
        for b_id in business_ids:
            business_id=b_id[0]
            # count the number of positive reviews of certain business_id
            cur.execute("SELECT count(*) From sentiment WHERE sentiment='pos'AND business_id=?",b_id)
            number_of_positive_reviews=cur.fetchone()[0]

            # count the number of negative reviews of certain business_id
            cur.execute("SELECT count(*) From sentiment WHERE sentiment='neg'AND business_id=?",b_id)
            number_of_negative_reviews=cur.fetchone()[0]

            # compute the percentage of positive and negative reviews
            number_of_reviews=int(number_of_positive_reviews)+int(number_of_negative_reviews)
            percentage_of_positive_reviews=float(number_of_positive_reviews)/float(number_of_reviews)
            percentage_of_negative_reviews=float(number_of_negative_reviews)/float(number_of_reviews)

            #insert data into review_stats table
            conn.execute("INSERT INTO {0} ({1},{2},{3},{4},{5}) VALUES (?,?,?,?,?);".
                     format(TABLE2_NAME, COLUMN_BUSINESS_ID,COLUMN_NUMBER_OF_POSITIVE_REVIEWS,COLUMN_NUMBER_OF_NEGATIVE_REVIEWS,COLUMN_PERCENTAGE_OF_POSITIVE_REVIEWS,COLUMN_PERCENTAGE_OF_NEGATIVE_REVIEWS),
                     (business_id,number_of_positive_reviews, number_of_negative_reviews, percentage_of_positive_reviews, percentage_of_negative_reviews))

        conn.commit()
        conn.close()

    # get the number of pos and neg reviews
    def get_number_of_reviews(self):
        conn=sqlite3.connect(DATABASE_NAME)
        sql="select number_of_positive_reviews, number_of_negative_reviews," \
            "percentage_of_positive_reviews,percentage_of_negative_reviews from review_stats where " \
            "business_id='{0}'".format(self.business_id)
        Rows=conn.execute(sql)
        # Only one record responding to each business_id
        for Row in Rows:
            self.number_of_positive_reviews=Row[0]
            self.number_of_negative_reviews=Row[1]
            self.percentage_of_positive_reviews=Row[2]
            self.percentage_of_negative_reviews=Row[3]
        return self
        return self
        conn.commit()
        conn.close()



