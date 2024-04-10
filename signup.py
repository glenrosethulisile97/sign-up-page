from flask import Flask,render_template,request,redirect,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/signup'
mongo = PyMongo(app)
db = mongo.db

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
       
        # Check if username or email already exists
        existing_user = db.user.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return 'Username or email already exists!'

        # Insert new user into the database
        signupdetails = {'username': username, 'email': email, 'password': password}
        db.user.insert_one(signupdetails)
        
        # Redirect to login page or homepage
        return redirect(url_for('login'))

    # Render the signup form template
    return render_template('SignUp.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

        