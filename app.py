from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import *
app = Flask(__name__ , static_url_path='/static')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)
db = mongo.db

# landing page
@app.route('/')
def landing():
        return render_template("homepage.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup(): 


    
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        existing_user = db.signup.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return 'Username or email already exists!'

        # Insert new user into the database
        signupdetails = {'username': username, 'email': email, 'password': password}
        db.signup.insert_one(signupdetails)
        
        # Redirect to login page or homepage
        return redirect(url_for('login'))

    # Render the signup form template
    return render_template('signup.html')

#Admin Signup
@app.route('/AdminSignup', methods=['GET', 'POST'])
def AdminSignup(): 


    
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        existing_user = db.Admin.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return 'Username or email already exists!'

        # Insert new user into the database
        signupdetails = {'username': username, 'email': email, 'password': password}
        db.Admin.insert_one(signupdetails)
        
        # Redirect to login page or homepage
        return redirect(url_for('AdminLogin'))

    # Render the signup form template
    return render_template('AdminSignup.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

       

    # Insert new user into the database
        user = {'username': username, 'password': password}
        if  db.signup.find_one(user):
            return redirect(url_for("HomePage"))
        else: redirect(url_for('signup'))
        

    # Render the login form template
    return render_template('loginpage.html')

#Admin login
@app.route('/AdminLogin', methods=['GET', 'POST'])
def AdminLogin():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

       

    # Insert new user into the database
        user = {'username': username, 'password': password}
        if  db.Admin.find_one(user):
            return redirect(url_for("Dashboard"))
        else: redirect(url_for('AdminSignup'))
        

    # Render the login form template
    return render_template('AdminLogin.html')
    
#Home Client
@app.route('/homepage', methods=['GET', 'POST'])
def HomePage():
    return render_template("landingpage.html")

#Dashboard
@app.route('/dasboard', methods=['GET', 'POST'])
def Dashboard():
    return render_template("adminDashboard.html")



@app.route('/contact')
def contact():
        return render_template("contact.html")

@app.route('/about')
def about():
        return render_template("about.html")


# #Display Service
# @app.route('/services')
# def services():
#         return render_template("service.html")

# Display AdminService
@app.route("/AdminServices", methods=["GET"])
def AdminServices():
    service = db.Services.find()  
    return render_template("AdminService.html", service = service)


# Display Service
@app.route("/services", methods=["GET"])
def services(): 
    return render_template("service.html",)



@app.route('/Concept Design')
def Concept_Design():
        return render_template("Concept Design.html")


@app.route('/Material and Finish')
def Material_Finish():
        return render_template("Material and Finish.html")


@app.route('/Styling and Decoration')
def Styling_Decoration():
        return render_template("Styling and Decoration.html")


@app.route('/Renovation and Remodeling')
def Renovation_Remodeling():
        return render_template("Renovation and Remodeling.html")

# @app.route('/Add_Conceptdesign')
# def Add_Conceptdesign():
#         return render_template("Add_Conceptdesign.html")

@app.route('/Add_Conceptdesign')
def add_item():   
    return render_template("Add_Conceptdesign.html")



@app.route('/AddOffice', methods=["POST"])
def add():   
    if request.method == 'POST':
        return render_template("AddOffice.html")
    return render_template("AddOffice.html")

#Add Booking
@app.route("/AddBooking", methods=["GET", "POST"])
def addbooking():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        color = request.form.get("color")
        offices = request.form.get("offices")
        size = request.form.get("size")

        booking = {"name": name, "email": email, "color": color, "offices": offices, "size": size}
        db.bookings.insert_one(booking)
        return redirect(url_for("Confirmation"))  # Redirect to the bookings page after successful submission

    return render_template("AddOffice.html")

#Booking
@app.route("/booking", methods=["POST", "GET"])
def getBooking():
    booking = []
    if request.method == 'GET':
        for i in db.bookings.find():
            booking.append(i)

    return render_template("booking.html", booking=booking)


     
@app.route("/confirmation", methods=["POST", "GET"] )
def Confirmation():
     if request.method == 'GET':
          booking = []

          for i in db.bookings.find():
            booking.append(i)
            
          

     return render_template("confirmation.html" , booking=booking )     

#delete booking
@app.route('/delete_booking', methods=['POST'])
def delete_booking():
    if request.method == 'POST':
        booking_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        booking_id = ObjectId(booking_id)
        # Delete the record from the collection
        result = db.bookings.delete_one({'_id': booking_id})
        if result.deleted_count == 1:
           booking = []

        for i in db.bookings.find():
                booking.append(i)
              
        return render_template('booking.html', booking=booking)
    else:
            return 'Record not found or could not be deleted.'
    
# /Editbooking/{6667ddac8e1e45947465f7a9}
    # editebooking/{booking_id}
@app.route('/Editbooking', methods=['POST'])
def Edit_booking():
    if request.method == 'POST':
        booking_id = request.form.get('booking_id')
        name = request.form.get("name")
        email = request.form.get("email")
        color = request.form.get("color")
        offices = request.form.get("offices")
        size = request.form.get("size")
        # Convert the string ID to ObjectId
        booking_id = ObjectId(booking_id)
        print("tests", booking_id)
        print("tests2 ", name)
        print("tests3", email)
        print("tests4", color)
        print("tests5", offices)
        print("tests6", size)
        # Edit the record from the collection

    result = db.bookings.update_one({'_id':booking_id},{'$set' :{"name": name, "email": email, "color": color, "offices": offices, "size": size}})
    
    booking=[]
    for i in db.bookings.find():
          booking.append(i)
          return render_template('booking.html', booking=booking)

@app.route('/Edit_booking1', methods=['POST'])
def Edit_booking1():
    if request.method == 'POST':
        booking_id = request.form.get('booking_id')
        name = request.form.get("name")
        email = request.form.get("email")
        color = request.form.get("color")
        offices = request.form.get("offices")
        size = request.form.get("size")
        print("tests second", booking_id)
        print("test second 2", name)
        print("test second 3", email)
        print("test second 4", color)
        print("test second 5", offices)
        print("test second 6", size)


    return render_template('Editbooking.html', name=name, email=email, color=color, offices=offices, size=size,  booking_id = booking_id,)


@app.route('/')
def getbooking():
    # Fetch data from the collection
    booking = db.bookings.find(booking)
    return render_template('booking.html', booking=booking)



# Add Service

@app.route("/AddService", methods=["GET", "POST"])
def AddService1():
     if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        
        service = { 'name': name, 'category': category, 'description': description}        
        db.Services.insert_one(service)
        service = db.Services.find()  
        return render_template("AdminService.html", service = service)  # Redirect to the bookings page after successful submission

     return render_template("AddService.html")


# Display service

@app.route("/service", methods=["POST", "GET"] )
def getservice():
     if request.method == 'GET':
          service = []

          for i in db.Services.find():
           service.append(i)

     return render_template("service.html" , i=service)
 
 
@app.route('/delete_AdminService', methods=['POST'])
def delete_service():
    if request.method == 'POST':
        services_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        services_id = ObjectId(services_id)
        # Delete the record from the collection
        result = db.Services.delete_one({'_id': services_id})
        if result.deleted_count == 1:
            service = []

            for i in db.Services.find():
               service.append(i)
            return render_template('AdminService.html', service=service)
        else:
            return 'Record not found or could not be deleted.'

# Edit service
@app.route('/EditService', methods=['POST'])
def Edit_Service():
    if request.method == 'POST':
        service_id = request.form.get('service_id')  # Get the ID of the record to delete
        name = request.form.get['name']
        category = request.form.get['category']
        description = request.form.get['description']
        # Convert the string ID to ObjectId
        service_id = ObjectId(service_id)
        # Edit the record from the collection
        
        result = db.Services.update_one({'_id': service_id},{'$set' :{'name' :name,'category': category, 'description':description,}})
        service= []


    service=[]
    for i in db.Services.find():
          service.append(i)
    return render_template('AdminService.html', service=service)


@app.route('/Edit_Service1', methods=['POST'])
def Edit_Service1():
    if request.method == 'POST':
      service_id = request.form.get('service_id')
      name = request.form.get['name']
      category = request.form.get['category']
      description = request.form.get['description']


        
    return render_template('EditService.html', name=name, category=category, description=description, service_id=service_id)

        
@app.route('/AdminserviceOf')
def Adminservice():
    # Fetch data from the collection
   service = db.Services.find
   return render_template('AdminService.html', x=service)


@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        # Get the review data from the request
        name = request.form.get('name')
        category= request.form.get('category')
        description = request.form.get('description')
        review_message = request.form.get('review_message')
        rating = int(request.form.get('rating'))

        # Prepare the review data as a dictionary
        review_data = {
            'name': name,
            'category': category,
            'description': description,
            'review_message': review_message,
            'rating': rating
        }

        # Save the review data to the MongoDB database
        mongo.db.review_collection.insert_one(review_data)

        # Redirect to the review_display route after submission
        return redirect(url_for('review_display'))

    # Render the review template on GET request
    return render_template('review.html')

@app.route('/review_display', methods=['GET'])
def review_display():
    # Retrieve data from MongoDB
    displays = mongo.db.review_collection.find()

    # Render the review_display template with the data
    return render_template('review.html', displays=displays)

    

if __name__ == "__main__":
    app.run(debug=True)
