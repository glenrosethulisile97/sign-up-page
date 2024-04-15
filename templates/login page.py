from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)
db = mongo.db

# Login Page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

        # Check if user exists
        existing_user = db.signup.find_one({'username': username, 'password': password})
        if existing_user:
            # Redirect to homepage or some other route
            return redirect(url_for('home'))
        else:
            # User not found, display error message
            return 'Invalid username or password'

    # Render the login form template
    return render_template('loginpage.html')

if __name__ == "__main__":
    app.run(debug=True)