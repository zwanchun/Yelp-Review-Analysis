__author__ = 'Wanchun Zhao'

import sqlite3
DATABASE_NAME = "reviews.db"

class Business:

    def __init__(self, business_id, full_address, categories, city, review_count, name, longitude, state, stars, latitude,type):
        self.business_id=business_id
        self.full_address=full_address
        self.categories=categories
        self.city=city
        self.review_count=review_count
        self.name=name
        self.longitude=longitude
        self.state=state
        self.stars=stars
        self.latitude=latitude
        self.type=type

    # get business_ids by business_name
    def get_ids_by_business_name(self):
        ids=list()
        conn=sqlite3.connect(DATABASE_NAME)
        sql="select distinct business_id from yelp_business where name='{0}'".format(self.name)
        Rows=conn.execute(sql)
        for Row in Rows:
            business=Business(Row[0],"","","","","","","","","","")
            ids.append(business)
        return ids
        conn.commit()
        conn.close()

    # get all distinct business_ids from sentiment table
    def get_all_business_ids(self):
        ids=list()
        conn=sqlite3.connect(DATABASE_NAME)
        sql="select distinct business_id from sentiment"
        Rows=conn.execute(sql)
        for Row in Rows:
            business=Business(Row[0],"","","","","","","","","","")
            ids.append(business)
        return ids
        conn.commit()
        conn.close()







