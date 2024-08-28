from flask import Flask, url_for, redirect, Response, request, render_template,flash
import re
from..models.user import Users

def landing():
    return render_template("homepage.html")

def AdminSignup():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Validate email format
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            flash('Invalid email format. Please try again.', 'error')
            return redirect(url_for('signup'))

        # Check if user already exists
        signupdetails = {'username': username, 'email': email, 'password': password}
        if not Users.create_user(signupdetails):
            flash('Email or username already exists. Please try again with different credentials.', 'error')
            return redirect(url_for('user.signup'))

        # Redirect to login page or homepage after successful signup
        return redirect(url_for('user.login'))

    # Render the signup form template if it's a GET request
    return render_template('signup.html')

def AdminLogin():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

        # Find the user by username and password
        existing_user = Users.find_user_by_username_and_password(username, password)
        
        if existing_user:
            # Redirect to homepage or some other route upon successful login
            return render_template("adminDashboard.html")
        else:
            # User not found, display error message
            flash('Invalid username or password.', 'error')
            return redirect(url_for('user.login'))

    # Render the login form template if it's a GET request
    return render_template('Adminlogin.html')

def signup():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

       # Validate email format
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            flash('Invalid email format. Please try again.', 'error')
            return redirect(url_for('user.signup'))


          # Check if user already exists
        signupdetails = {'username': username, 'email': email, 'password': password}
        if not Users.create_user(signupdetails):
            flash('Email or username already exists. Please try again with different credentials.', 'error')
            return redirect(url_for('user.signup'))
          
# Redirect to login page or homepage after successful signup
        return redirect(url_for('user.login'))

    # Render the signup form template if it's a GET request
    return render_template('signup.html')


def login():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

       # Find the user by username and password
        existing_user = Users.find_user_by_username_and_password(username, password)
        
        if existing_user:
            # Redirect to homepage or some other route upon successful login
            return render_template("landingpage.html")
        else:
            # User not found, display error message
            flash('Invalid username or password.', 'error')
            return redirect(url_for('user.login'))
    # Render the login form template
    return render_template('loginpage.html')

def landing():
        return render_template("homepage.html")
