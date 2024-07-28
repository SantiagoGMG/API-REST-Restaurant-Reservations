#Aqui debe de ir para consultar el html

from flask import Blueprint, render_template , session
from app.controller import controllerDB

global_scope = Blueprint("views", __name__)


@global_scope.route("/", methods=['GET'])
def home():
    session['key'] = 'value'
    data = controllerDB.readRow()
    return render_template("home.html",dates = data)
"""
@global_scope.route('/edit/<string:DateToReserve_date>', methods=['GET'])
def edit_reservation(DateToReserve_date):
    session['key'] = 'value'
    DataFound = controllerDB.searchForDate(DateToReserve_date)
    return render_template("edit_reservation.html", reservation = DataFound)
"""