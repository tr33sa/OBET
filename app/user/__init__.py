from flask import Blueprint

user = Blueprint('user', __name__, template_folder="templates")

from . import views_user, views_manageUsers, views_editProfile