from mainapp import bootstrap,db
from flask import Blueprint

authentication = Blueprint("authenticate",__name__,template_folder="templates")

from auth import views