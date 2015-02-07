__author__ = 'Wanchun Zhao'

import sqlite3

TABLE_NAME = "yelp_review"
DATABASE_NAME = "reviews.db"

class Review:
    # constructor
    def __init__(self, review_id, user_id, stars, date, text, type, business_id, votes_funny, votes_useful, votes_cool):
        self.review_id=review_id
        self.user_id=user_id
        self.stars=stars
        self.date=date
        self.text=text
        self.type=type
        self.business_id=business_id
        self.votes_funny=votes_funny
        self.votes_useful=votes_useful
        self.votes_cool=votes_cool

    # get review_id, business_id, text from yelp_review table
    def get_reviews(self,limit):
        Reviews=list()
        conn=sqlite3.connect(DATABASE_NAME)
        sql="SELECT review_id, business_id,text FROM yelp_review limit "+limit
        Rows=conn.execute(sql)
        for Row in Rows:
            review = Review(Row[0], "", "","",Row[2],"",Row[1],"","","")
            Reviews.append(review)
        return Reviews

        conn.commit()
        conn.close()

    # Using business_id and sentiment to get review texts from yelp_review, there is a limit
    def get_reviews_by_business_id_and_sentiment(self, business_id, sentiment, limit):
        Reviews=list()
        conn=sqlite3.connect(DATABASE_NAME)
        sql="select yelp_review.text from yelp_review, sentiment where yelp_review.review_id =sentiment.review_id and" \
            " sentiment.sentiment = '{0}' and sentiment.business_id = '{1}' limit {2}".format(sentiment,business_id, limit)
        Rows=conn.execute(sql)
        for Row in Rows:
            review = Review("", "", "","",Row[0],"","","","","")
            Reviews.append(review)
        return Reviews

    # Using business_id to get reviews from yelp_review table
    def get_reviews_by_business_id(self):
        Reviews=list()
        conn=sqlite3.connect(DATABASE_NAME)
        sql="select * from yelp_review where yelp_review.business_id = '{0}'".format(self.business_id)
        Rows=conn.execute(sql)
        for Row in Rows:
            review = Review(Row[0], Row[1], Row[2],Row[3],Row[4],Row[5],Row[6],Row[7],Row[8],Row[9])
            Reviews.append(review)
        return Reviews

    # using review_id in sentiment table to get review text from yelp_review table
    def get_all_reviews_by_business_id_and_sentiment(self, business_id, sentiment):
        Reviews=list()
        conn=sqlite3.connect(DATABASE_NAME)
        sql="select yelp_review.text from yelp_review, sentiment where yelp_review.review_id =sentiment.review_id and" \
            " sentiment.sentiment = '{0}' and sentiment.business_id = '{1}'".format(sentiment,business_id)
        Rows=conn.execute(sql)
        for Row in Rows:
            review = Review("", "", "","",Row[0],"","","","","")
            Reviews.append(review)
        return Reviews






