#!/usr/bin/python3
"""Create views for the Student object - handle all the default Restful API actions."""
import models
import datetime
from flask import jsonify, request, abort, url_for, redirect
from models import storage
from models.student import Student
from routes.v1.views import app_views, auth
from flask_jwt_extended import jwt_required, JWTManager, create_access_token, create_refresh_token


jwt = JWTManager()
app_conf = "kimathi"

def authenticate(email, password):
    students = storage.all(Student)
    for student in students.values():
        if student.email == email and student.password == password:
            return student

# Identity function
# a create a new student
@app_views.route('/students', methods=["GET", 'POST'], strict_slashes=False)
def create_student():
    """Create a new student."""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if 'first_name' not in request.get_json():
        return jsonify({"error": "Missing first_name"}), 400
    if 'last_name' not in request.get_json():
        return jsonify({"error": "Missing last_name"}), 400
    if 'phone' not in request.get_json():
        return jsonify({"error": "Missing phone number"}), 400
    if 'password' not in request.get_json():
        return jsonify({"error": "Missing password"}), 400
    if 'address' not in request.get_json():
        return jsonify({"error": "Missing address"}), 400
    if 'city' not in request.get_json():
        return jsonify({"error": "Missing city"}), 400
    if 'state' not in request.get_json():
        return jsonify({"error": "state"}), 400
    if 'zip_code' not in request.get_json():
        return jsonify({"error": "Missing zip code"}), 400

    data = request.get_json()
    new_student = Student(**data)
    new_student.save()
    return jsonify(new_student.to_dict()), 201

@app_views.route("/", methods=["GET"], strict_slashes=False)
def hello():
    return jsonify({"Hello": "World"})



@auth.route('/login', methods=["POST"], strict_slashes=False)
def login():
    """Login a user"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if 'email' not in request.get_json():
        return jsonify({"error": "Missing email"}), 400
    if 'password' not in request.get_json():
        return jsonify({"error": "Missing password"}), 400
    data = request.get_json()
    email = data['email']
    password = data['password']
    student = authenticate(email, password)
    if student is None:
        return jsonify({"error": "Invalid email or password"}), 401
        # generate a token for the user and an espiry date
    token = create_access_token(identity=student.address)
    refresh_token = create_refresh_token(identity = student.address)
    # redirect to the protected page
    return jsonify({"Message": "Login succesfful",
                   "token": {
                "access_token": token,
                    "refresh_token": refresh_token,
                "expires_in": 3600
                }}), 201
# the protected page
@app_views.route('/protected')
@jwt_required()
def user_protected():
    return jsonify({"Hello": "World"})
