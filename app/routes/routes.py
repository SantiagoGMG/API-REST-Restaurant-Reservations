#Aqui debe de ir para consultar el html

from flask import Blueprint, render_template

global_scope = Blueprint("views", __name__)


@global_scope.route("/", methods=['GET'])
def home():
    """Landing page route."""

    parameters = {"title": "Flask and Jinja Practical work",
                  "description": "This is a simple page made for implement the basics concepts of Flask and Jinja2"
                  }

    return render_template("home.html",**parameters)