
#!/usr/bin/python3
"""Thid module defines the views for the properties endpoint"""

from flask import jsonify, request
from models import storage
from models.landlord import Landlord
from models.property import Properties
from routes.v1.views import app_views
from flask_jwt_extended import jwt_required

# endpoint to create a new property
# All the returns are in JSON format
@app_views.route('/landlords/<landlord_id>/cities/<city_id>/properties', methods=['POST'], strict_slashes=False)
def create_property(landlord_id, city_id):
    """function to create a new property"""
    landlord = storage.get("Landlord", landlord_id)
    if landlord is None:
        return jsonify({"error": "Notfound"}), 404
    city = storage.get("City", city_id)
    if city is None:
        return jsonify({"error": "City Not Found"}), 404
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    if 'address' not in request.get_json():
        return jsonify({"error": "Missing address"}), 400
    if 'zip_code' not in request.get_json():
        return jsonify({"error": "Missing zip code"}), 400
    if 'description' not in request.get_json():
        return jsonify({"error": "Missing description"}), 400
    if 'price' not in request.get_json():
        return jsonify({"error": "Missing price"}), 400
    data = request.get_json()
    data['landlord_id'] = landlord_id
    data['city_id'] = city_id
    property = Properties(**data)
    property.save()
    return jsonify(landlord.to_dict()), 201

@app_views.route('/landlords/<landlord_id>/properties', methods=['GET'], strict_slashes=False)
def get_properties(landlord_id):
    """function to get all properties"""
    landlord = storage.get("Landlord", landlord_id)
    if landlord is None:
        return jsonify({"error": "Not found"}), 404
    properties = [property.to_dict() for property in landlord.properties]
    return jsonify(properties), 200

# endpoint to get a property by id
@app_views.route('/landlords/<landlord_id>/properties/<property_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_property(landlord_id, property_id):
    """function to get a property by id"""
    landlord = storage.get("Landlord", landlord_id)
    if landlord is None:
        return jsonify({"Error": "Not Found"}), 404
    property = storage.get("Properties", property_id)
    if property is None:
        return jsonify({"Error": "Not Found"}), 404
    return jsonify(property.to_dict()), 200

# endpoint to update a property
@app_views.route('/landlords/<landlord_id>/properties/<property_id>', methods=['PUT'], strict_slashes=False)
def update_property(landlord_id, property_id):
    """function to update a property"""
    landlord = storage.get("Landlord", landlord_id)
    if landlord is None:
        return jsonify({"error": "Not found"}), 404
    property = storage.get("Properties", property_id)
    if property is None:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        setattr(property, key, value)
    property.save()
    return jsonify(property.to_dict()), 200
# endpoint to delete a property
@app_views.route('/landlords/<landlord_id>/properties/<property_id>', methods=['DELETE'], strict_slashes=False)
def delete_property(landlord_id, property_id):
    """function to delete a property"""
    landlord = storage.get("Landlord", landlord_id)
    if landlord is None:
        return jsonify({"error": "Not found"}), 404
    property = storage.get("Properties", property_id)
    if property is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(property)
    storage.save()
    return jsonify({}), 200

# endpoint to get all properties by city
