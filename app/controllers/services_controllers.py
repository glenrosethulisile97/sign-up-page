from flask import request, render_template
from ..models import services

def admin_services():
    services = services()
    return render_template("AdminService.html", services=services)

def services():
    return render_template("service.html")

def concept_design():
    return render_template("Concept Design.html")

def material_finish():
    return render_template("Material and Finish.html")

def styling_decoration():
    return render_template("Styling and Decoration.html")

def renovation_remodeling():
    return render_template("Renovation and Remodeling.html")

def add_concept_design():
    return render_template("Add_Conceptdesign.html")

def add_office():
    if request.method == 'POST':
        # Handle the post request if needed
        pass
    return render_template("AddOffice.html")