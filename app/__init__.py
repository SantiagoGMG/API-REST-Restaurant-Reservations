from flask import Flask
from config import Config
from .routes import api_scope , global_scope

app = Flask(__name__, template_folder='views/templates')
app.config.from_object(Config)
app.register_blueprint(api_scope)
app.register_blueprint(global_scope)
