from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
app_views = Blueprint('app_views', __name__, url_prefix='/views')

from models import storage
from models.student import Student

from routes.v1.views.student import *

