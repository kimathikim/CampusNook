#!/usr/bin/python3
"""This module defines the views for state filters for student to get all the properties in that state"""
 
from flask import jsonify, request
from models import storage
from models.landlord import Landlord
from models.property import Properties
from models.state import State
from routes.v1.views import app_views
from flask_jwt_extended import jwt_required

# endpoint to print ouit all the properties in the state id
@app_views.route("/property/state/<state_id>", methods=["GET"], slash=False)
def property_state(state_id):
    """This function returns all the properties in a state"""
    state = storage.get("State", state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    properties = state.properties
    return jsonify([property.to_dict() for property in properties])


# endpoint to search properties by state names
@app_views.route("/property/state", methods=["GET"], slash=False)
def property_state_name():
    """This function returns all the properties in a state"""
    state_name = request.args.get("name")
    if state_name is None:
        return jsonify({"error": "Not found"}), 404
    state = storage.get("State", state_name)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    properties = state.properties
    return jsonify([property.to_dict() for property in properties])


# endpoint to print out all the properties in the city
@app_views.route("/property/city/<city_id>", methods=["GET"], slash=False)
def property_city(city_id):
    """This function returns all the properties in a city"""
    city = storage.get("City", city_id)
    if city is None:
        return jsonify({"error": "Not found"}), 404
    properties = city.properties
    return jsonify([property.to_dict() for property in properties])


