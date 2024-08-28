from app import PyMongo
from .. import mongo

class Review:
 
 def save_review(review_data):
   mongo.db.review_collection.insert_one(review_data)

 def get_reviews():
    return mongo.db.review_collection.find()