# src/routes/app.py
import sys
import os
from flask import Flask , jsonify

# Añadir la carpeta project_root/src al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.models.DateToReserve import DateToReserve

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message" : 'pong'})

@app.route('/reserve', methods = ['GET'])
def reserve():
    return jsonify({ "message": "date available to reserve", "DateToReserve": DateToReserve })

@app.route('/reserve/<string:DateToReserve_date>')
def getReserve(DateToReserve_date):
    DateToReserveFound = [date for date in DateToReserve if date['date']==DateToReserve_date]
    if (len(DateToReserveFound) > 0):
        return jsonify({'Date available to reserve '+ DateToReserve_date :DateToReserveFound[0]})
    else:
        return jsonify({"message":'Date unavailable'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
