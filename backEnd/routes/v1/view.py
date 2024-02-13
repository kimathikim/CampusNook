# routes/v1/views.py
from flask import Blueprint
from routes.v1 import create_app

app, app_conf = create_app()

# Now you can access app_conf
print(app_conf['SECRET_KEY'])
