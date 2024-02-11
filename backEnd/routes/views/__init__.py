from flask import Blueprint
auths = Blueprint('auths', __name__, url_prefix='/auths')
app_views = Blueprint('app_views', __name__, url_prefix='/views')

