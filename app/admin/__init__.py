from flask import Blueprint
import redis
db = redis.Redis('localhost')
admin = Blueprint('admin',__name__, template_folder="template")
from . import view

