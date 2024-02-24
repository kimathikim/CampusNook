#!/usr/bin/python5
"""An app to register blueprints and start flask"""

from flask import Flask, make_response, jsonify, request, url_for, redirect
from flask_cors import CORS
from models import storage
from routes.v1.views.student import *
from models.student import Student
import datetime


from os import getenv
def create_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = app_conf
    CORS(app, origins='0.0.0.0')

    from routes.v1.views import app_views, auth
    app.register_blueprint(app_views)
    app.register_blueprint(auth)



    jwt.init_app(app)


    @app.teardown_appcontext
    def tear_down(self): 
        """Remove the current SQLAlchemy session"""
        storage.close()

    @app.route("/")
    def hello():
        """Return a hello message"""
        return jsonify({"Hello": "World"})


    @app.errorhandler(404)
    def not_found(error):
        """Return a 404 error"""
        return make_response(jsonify({"error": "Not found"}), 404)
    return app
