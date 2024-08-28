from flask import Flask
from flask_pymongo import pymongo
from .config import config

mongo = pymongo()

def create_app():
    app=Flask(__name__)
    app.config.from_object(config)

    mongo.init_app(app)


    return app