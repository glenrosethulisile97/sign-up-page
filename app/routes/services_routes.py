from flask import Blueprint
from ..controllers import services_controllers

app = Blueprint ('services',__name__)

app.route("/landingpage", methods=['GET',])(services_controllers.landing)


app.route("/services", methods=['GET','POST'])(services_controllers.services)


app.route('/Concept Design',methods=['GET', 'POST'])(services_controllers.Concept_Design)


app.route('/Material and Finish',methods=['GET', 'POST'])(services_controllers.Material_Finish)


app.route('/Styling and Decoration',methods=['GET', 'POST'])(services_controllers.Styling_Decoration)


app.route('/Renovation and Remodeling',methods=['GET', 'POST'])(services_controllers.Renovation_Remodeling)