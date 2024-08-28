
from flask import Blueprint
from ..controllers import services_controllers


service_bp = Blueprint('service', __name__)

service_bp.route("/AdminServices", methods=["POST","GET"])(services_controllers.AdminServices)
service_bp.route("/services", methods=["POST","GET"])(services_controllers.services)
service_bp.route('/Concept Design', methods=["POST","GET"])(services_controllers.concept_design)
service_bp.route('/Material and Finish', methods=["POST","GET"])(services_controllers.material_finish)
service_bp.route('/Styling and Decoration', methods=["POST","GET"])(services_controllers.styling_decoration)
service_bp.route('/Renovation and Remodeling', methods=["POST","GET"])(services_controllers.renovation_remodeling)
service_bp.route('/Add_Conceptdesign', methods=["POST","GET"])(services_controllers.add_concept_design)
service_bp.route('/AddOffice', methods=["GET", "POST"])(services_controllers.add_office)
service_bp.route('/about', methods=["GET", "POST"])(services_controllers.about)
service_bp.route('/contact', methods=["GET", "POST"])(services_controllers.contact)


