from..import mongo

class service:

    def create_services(data):
        product_id  = mongo.db.services.insert_one(data).Inserted_id
        return str(services_id)
    
    def get_all_services():
        return list(mongo.db.services.find({},{'_id',0}))