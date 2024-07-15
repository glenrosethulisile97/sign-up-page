from ..import mongo



class landing:

   def AdminServices():
    service = mongo.db.Services.find()  
    return list("AdminService.html", service = service)