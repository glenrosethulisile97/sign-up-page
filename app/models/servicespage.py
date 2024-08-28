from .. import mongo

class products:

 def get_the_service():
    return mongo.db.services.find()