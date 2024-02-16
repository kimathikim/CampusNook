#!/usr/bin/python3
"""Thid module defines the views for the state endpoint"""
from flask import jsonify, request, request_started
from models import storage
from models.state import State
from models.property import Properties
from routes.v1.views import app_views
from flask_jwt_extended import jwt_required


# create a new state

@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """This creates a new state object"""
    data = request.get_json()
    if not data:
        return jsonify({"Error": "Not JSON"}), 400
    
    state_name = data.get("name")
    if not state_name:
        return jsonify({"Error": "State name missing"}), 400
    
    state = State(name=state_name)
    state.save()
    
    return jsonify(state.to_dict()), 201

# get
# update
# delete
#
