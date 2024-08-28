from flask import request, render_template, redirect, url_for
from ..models.AdminService import Service
from bson.objectid import*

def add_service():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        
        service = { 'name': name, 'category': category, 'description': description }        
        Service.add_service_to_db(service)
        return redirect(url_for('Adminservice.Adminservice'))  # Redirect to the admin services page after successful submission

    return render_template("AddService.html")

def get_service():
    service = Service.get_all_services()
    return render_template("service.html", service=service)

# def delete_service():
#     if request.method == 'POST':
#         service_id = request.form.get('delete_id')
#         Service(service_id)
#         return redirect(url_for('AdminService_bp'))

def delete_service(): 
    if request.method == 'POST':
     services_id = request.form.get('delete_id')   
     services_id = ObjectId(services_id)
     result = Service.delete_service(services_id)
     if result.deleted_count == 1:
         return redirect(url_for('Adminservice.Adminservice'))
     else:
         return 'record not found or could not be deleted' 

def edit_service():
    if request.method == 'POST':
        service_id = request.form.get('service_id')
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        
        Service(service_id, name, category, description)
        return redirect(url_for('AdminService_bp'))

def edit_service_form():
    if request.method == 'POST':
        service_id = request.form.get('service_id')
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        
        return render_template('EditService.html', name=name, category=category, description=description, service_id=service_id)

def Adminservice():
    # Fetch data from the collection
   service = list(Service.display_services())
   return render_template('AdminService.html', service=service)

def Dashboard():
    return render_template("adminDashboard.html")

