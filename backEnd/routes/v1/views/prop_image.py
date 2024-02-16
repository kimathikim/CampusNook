 #!/usr/bin/python3
"""Thid module defines the views for the prop_images endpoint"""
from flask import jsonify, request
from models import storage
from models.prop_images import Prop_images
from models.property import Properties
from routes.v1.views import app_views
from flask_jwt_extended import jwt_required
import base64
# endpoint to create image for the chosen @propert
@app_views.route('/properties/<property_id>/images', methods=['POST'], strict_slashes=False)
def create_images(property_id):
    """function to create a new image"""
    property = storage.get("Properties", property_id)
    if property is None:
        return jsonify({"error": "Property not found"}), 404
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if 'image' not in request.get_json():
        return jsonify({"error": "Missing image"}), 400
    data = request.get_json()
    data['property_id'] = property_id
    image_base64 = data['image']
    image_bin = base64.b64decode(image_base64)
    data['image'] = image_bin
    image = Prop_images(**data)
    image.save()
    return jsonify(property.to_dict()), 201

# endpoint to get all the images of the chosen @property
@app_views.route('/properties/<property_id>/images', methods=['GET'], strict_slashes=False)
def get_images(property_id):
    """function to get all the images of a chosen property"""
    # check if the prop exists
    prop = storage.get("Properties", property_id)
    if prop is None:
        return jsonify({"Error": "Property does not exist"}), 404
    # fetch data from images table
    images = []
    for image in prop.prop_images:
        image_dict = image.to_dict()
        # encode image from binaly to base64
        image_dict['image'] = base64.b64encode(image_dict['image']).decode('utf-8')
        images.append(image_dict)

    return jsonify(images), 200

