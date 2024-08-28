from flask import Blueprint
from ..controllers import AdminService_controllers

AdminService_bp = Blueprint('Adminservice', __name__)

AdminService_bp.route("/AddService", methods=["GET", "POST"])(AdminService_controllers.add_service)
AdminService_bp.route("/service", methods=['POST', 'GET'])(AdminService_controllers.get_service)
AdminService_bp.route("/delete_AdminService", methods=['POST', 'GET'])(AdminService_controllers.delete_service)
AdminService_bp.route("/EditService", methods=["POST", 'GET'])(AdminService_controllers.edit_service)
AdminService_bp.route("/Edit_Service1", methods=["POST", 'GET'])(AdminService_controllers.edit_service_form)
AdminService_bp.route("/AdminService", methods=['POST',"GET"])(AdminService_controllers.Adminservice)