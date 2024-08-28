from .. import mongo
from app import PyMongo
from bson.objectid import ObjectId


class Service:

    def add_service_to_db(service):
     return mongo.db.Services.insert_one(service)

    def get_all_services():
     return mongo.db.Services.find()

    # def delete_service_by_id(service_id ):
    #  return mongo.db.Services.delete_one({ObjectId:service_id})
    
    def display_services():
      return mongo.db.Services.find()


    def update_service_by_id(service_id, name, category, description):
     Service_id = ObjectId(service_id)
     PyMongo.update_one({'_id': service_id}, {'$set': {'name': name, 'category': category, 'description': description}})

    def delete_service(delete_service_id):
       return mongo.db.Services.delete_one({'_id':delete_service_id})