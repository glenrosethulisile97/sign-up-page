from ..import mongo

class Users:

  
    def create_user(signupdetails):
        existing_user = Users.find_user_by_username_or_email(signupdetails['username'], signupdetails['email'])
        if existing_user:
            return False  # User already exists
        else:
            # Insert the new user into the database
            mongo.db.signup.insert_one(signupdetails)
            return True  # User created successfully

  
    def find_user_by_username_or_email(username, email):
        return mongo.db.signup.find_one({'$or': [{'username': username}, {'email': email}]})

  
    def find_user_by_username_and_password(username, password):
        return mongo.db.signup.find_one({'username': username, 'password': password})

 
    def get_user_by_email(email):
        return mongo.db.signup.find_one({'email': email})
    
    
    
    
    

  

