from flask import Flask, Blueprint

app = Flask(__name__)
app.config.from_pyfile('conf.py')
from app import routes
from .admin import admin

app.register_blueprint(admin,url_prefix="/admin")

#admin = Blueprint("admin",__name__)
#admin.register_blueprint(admin,url_prefix='/admin')


