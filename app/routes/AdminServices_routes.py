from flask import Blueprint
from controllers import AdminServices_controllers

service_bp = Blueprint('service', __name__)

service_bp.route("/AddService", methods=["GET", "POST"])(AdminServices_controllers.add_service)
service_bp.route("/service", methods=["GET"])(AdminServices_controllers.get_service)
service_bp.route("/delete_AdminService", methods=["POST"])(AdminServices_controllers.delete_service)
service_bp.route("/EditService", methods=["POST"])(AdminServices_controllers.edit_service)
service_bp.route("/Edit_Service1", methods=["POST"])(AdminServices_controllers.edit_service_form)
service_bp.route("/AdminServices", methods=["GET"])(AdminServices_controllers.admin_services)