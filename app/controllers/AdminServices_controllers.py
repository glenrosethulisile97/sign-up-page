from flask import request, render_template, redirect, url_for
from ..models import AdminServices

def add_service():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        
        service = { 'name': name, 'category': category, 'description': description }        
        AdminServices(service)
        return redirect(url_for('service.admin_services'))  # Redirect to the admin services page after successful submission

    return render_template("AddService.html")

def get_service():
    services = AdminServices()
    return render_template("service.html", services=services)

def delete_service():
    if request.method == 'POST':
        service_id = request.form.get('delete_id')
        AdminServices(service_id)
        return redirect(url_for('service.admin_services'))

def edit_service():
    if request.method == 'POST':
        service_id = request.form.get('service_id')
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        
        AdminServices(service_id, name, category, description)
        return redirect(url_for('service.admin_services'))

def edit_service_form():
    if request.method == 'POST':
        service_id = request.form.get('service_id')
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        
        return render_template('EditService.html', name=name, category=category, description=description, service_id=service_id)

def admin_services():
    services =AdminServices()
    return render_template('AdminService.html', services=services)