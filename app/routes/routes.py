#Aqui debe de ir para consultar el html

from flask import Blueprint, render_template , session

global_scope = Blueprint("views", __name__)


@global_scope.route("/", methods=['GET'])
def home():
    session['key'] = 'value'
    return render_template("home.html")
