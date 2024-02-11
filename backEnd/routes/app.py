#!/usr/bin/python3
"""An app to register blueprints and start flask"""

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from routes.views import auths, app_views
from os import getenv

app = Flask(__name__)
CORS(app, origins='0.0.0.0')
app.register_blueprint(auths)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down(self):
    """Remove the current SQLAlchemy session"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Return a 404 error"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(
        host=getenv('CN_HOST', '0.0.0.0'),
        port=int(getenv('CN_PORT', 5000)),
        threaded=True,
        debug=True
    )
