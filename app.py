from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

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

@app.route('/homepage', methods=['GET', 'POST'])
def HomePage():
    return render_template("landingpage.html")

@app.route('/contact')
def contact():
        return render_template("contact.html")

@app.route('/about')
def about():
        return render_template("about.html")

@app.route('/services')
def services():
        return render_template("service.html")


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)