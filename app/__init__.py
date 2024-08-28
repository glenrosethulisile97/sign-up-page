from flask import Flask
from flask_pymongo import PyMongo
from.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)

    with app.app_context():
       from .routes import user_routes, services_routes, bookings_routes, reviews_routes,AdminService_routes
       app.register_blueprint(user_routes.app)
       app.register_blueprint(services_routes.service_bp)
       app.register_blueprint(bookings_routes.booking_bp)
       app.register_blueprint(reviews_routes.review_bp)
       app.register_blueprint(AdminService_routes.AdminService_bp)
      #  app.register_blueprint(about_routes.about_bp)
      #  app.register_blueprint(contact_routes.contact_bp)
       

       return app



