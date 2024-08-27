from app import PyMongo
from bson.objectid import ObjectId

def add_service_to_db(service):
    add_service_to_db.insert_one(service)

def get_all_services():
    return list(add_service_to_db.find())

def delete_service_by_id(service_id):
    service_id = ObjectId(service_id)


def update_service_by_id(service_id, name, category, description):
    service_id = ObjectId(service_id)
    PyMongo.update_one({'_id': service_id}, {'$set': {'name': name, 'category': category, 'description': description}})