from flask import jsonify,request
from ..models.services import services


def create_services():

    data = {
        "name": request.json.get("name"),
        "category": request.json.get("category"),
        "description": request.json.get("description"),
    }


    services_id = services.create_app(data)

    return jsonify({"message": "service added","service id": service_id})


def get_all_services():
    services = 