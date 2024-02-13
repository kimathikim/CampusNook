#!/usr/bin/python3
"""Create views for the landlord object - handle all the default Restful API actions."""
from flask import jsonify, request
from models import storage
from models.landlord import Landlord
from routes.v1.views import app_views, auth
from routes.v1.views.student import jwt, app_conf
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

def authenticate(email, password):
    landlord = storage.all(Landlord )
    for landlord in landlord.values():
        if landlord.email == email and landlord.password == password:
            return landlord


# register a new landlord POST and all the returns are in JSON format
@app_views.route('/landlords', methods=['POST'], strict_slashes=False)
def create_landlord():
    """Create a new landlord."""
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
    landlord = Landlord(**data)
    landlord.save()
    return jsonify(landlord.to_dict()), 201

@auth.route('/landlord/login', methods=["POST"], strict_slashes=False)
def landlord_login():
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
    landlord = authenticate(email, password)
    if landlord is None:
        return jsonify({"error": "Invalid email or password"}), 401
        # generate a token for the user and an espiry date
    token = create_access_token(identity=landlord.address)
    refresh_token = create_refresh_token(identity = landlord.address)
    # redirect to the protected page
    return jsonify({"Message": "Login succesfful",
                   "token": {
                "access_token": token,
                    "refresh_token": refresh_token,
                "expires_in": 60
                }}), 201

@app_views.route('/landlord/protected')
@jwt_required()
def landlord_protected():
    return jsonify({"Hello": "World"})
