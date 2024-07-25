from flask import Flask , send_from_directory
from config import Config
from .routes import api_scope , global_scope

# el static_folder es para ingresar a la carpeta static  

app = Flask(__name__, template_folder='views/templates',static_folder='views/static')
app.config.from_object(Config)
app.register_blueprint(api_scope)
app.register_blueprint(global_scope)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('views/static', path)