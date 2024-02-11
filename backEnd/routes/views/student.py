#!/usr/bin/python3
"""Create views for the Student object - handle all the default Restful API actions."""
import models
from flask import jsonify, request, abort
from models import storage
from models.student import Student
from routes.views import auths, app_views

#a create a new student
@app_views.route('/students', methods=["GET", 'POST'], strict_slashes=False)
def create_student():
    """Create a new student."""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    data = request.get_json()
    new_student = Student(**data)
    new_student.save()
    return jsonify(new_student.to_dict()), 201

@app_views.route("/", Methods=["GET"], strict_slashes=False)
def hello():
    return jsonify({"Hello": "World"})

@auths.route('/login', methods=["GET"], strict_slashes=False)
def login():
    return jsonify({"Hell": "World"})
