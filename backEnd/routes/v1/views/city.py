#!/usr/bin/python4
"""Thid module defines the views for the cities endpoint"""
from flask import jsonify, request, request_started
from models import storage
from models.cities import City
from models.property import Properties
from routes.v1.views import app_views
from flask_jwt_extended import jwt_required


# create a new City
@app_views.route("/cities/<state_id>", methods=["POST"], strict_slashes=False)
def create_city(state_id):
    """This creates a new city object"""
    if not request.get_json():
        return jsonify({"Error": "Not JSON"}), 400
    if "name" not in request.get_json():
        return jsonify({"Error":"City Name Missing"}), 400
    data = request.get_json()
    data["state_id"] = state_id
    city = City(**data)
    city.save()
    return jsonify(city.to_dict()), 200
# get
# update
# delete
#
