from flask import Blueprint
from ..controllers import user_controllers


app = Blueprint ('user',__name__)


app.route("/", methods=['GET','POST'])(user_controllers.landing)
app.route("/signup", methods = ['POST','GET'])(user_controllers.signup)
#Admin Signup
app.route('/AdminSignup', methods=['GET', 'POST'])(user_controllers.AdminSignup)
app.route('/login', methods=['GET', 'POST'])(user_controllers.login)
#Admin login
app.route('/AdminLogin', methods=['GET', 'POST'])(user_controllers.AdminLogin)



















