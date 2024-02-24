from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
app_views = Blueprint('app_views', __name__, url_prefix='/views')

from models import storage
from models.student import Student
from models.landlord import Landlord
from models.property import Properties
from models.prop_images import Prop_images
from models.cities import City
from models.state import State

from routes.v1.views.student import *
from routes.v1.views.landlord import *
from routes.v1.views.properties import *
from routes.v1.views.prop_image import *
from routes.v1.views.city import *
from routes.v1.views.state import *
from routes.v1.views.filters import *
