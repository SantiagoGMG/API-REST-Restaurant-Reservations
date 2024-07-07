# src/routes/app.py
import sys
import os
from flask import Flask , jsonify , request , Blueprint

# Añadir la carpeta project_root/src al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.database.DateToReserve import DateToReserve

#app = Flask(__name__)
api_scope = Blueprint("api", __name__)

@api_scope.route('/ping', methods = ['GET'])
def ping():
    return jsonify({'message' : 'pong'})

@api_scope.route('/reserve', methods = ['GET'])
def reserve():
    return jsonify({ 'message': "date available to reserve", "DateToReserve": DateToReserve })

@api_scope.route('/reserve/<string:DateToReserve_date>', methods = ['GET'])
def getReserve(DateToReserve_date):

    DateToReserveFound = [date for date in DateToReserve if date['date']==DateToReserve_date]
    if (len(DateToReserveFound) > 0):
        return jsonify({'Date available to reserve '+ DateToReserve_date :DateToReserveFound[0]})
    else:
        return jsonify({'message':'Date unavailable'})

@api_scope.route('/reserve' , methods = ['POST'])
def addReserve():
    newReserve = {
        "date": request.json["date"],
        "table available" : request.json["table available"]
    }
    DateToReserve.append(newReserve)
    
    return jsonify({'message': "Reserve added sucessfully", "Reserve":DateToReserve})

@api_scope.route ('/reserve/<string:DateToReserve_date>', methods = ['PUT'])
def editReserve (DateToReserve_date):
    DateToReserveFound = [ reserve for reserve in DateToReserve if reserve['date'] == DateToReserve_date ]

    if (len(DateToReserveFound) > 0):

        for date in DateToReserve:
            if date.get('date') == request.json['date']:
                Exists = True
                break
        if(not Exists):
            DateToReserveFound[0]['date'] = request.json['date']
            DateToReserveFound[0]['table available'] = request.json['table available']
            return jsonify({'message' : 'Reserve Updated', 'reserve':DateToReserveFound[0]})
        else:
            return jsonify('Esa fecha ya existe y no coincide con la fecha que estas actualizando')
    else:
        return jsonify({'message': 'Product not found'})
        
@api_scope.route('/reserve/<string:DateToReserve_date>', methods = ['DELETE'])
def deleteReserve (DateToReserve_date):
    DateToReserveFound =[ reserve for reserve in DateToReserve if reserve['date'] == DateToReserve_date]
    if(len(DateToReserveFound) > 0):
        DateToReserve.remove(DateToReserveFound)
        return jsonify ({'message': 'Reserve Deleted', 'Reserve': DateToReserve})
    else:    
        return jsonify ({'message': 'Reserve not found'})

""""
if __name__ == '__main__':
    app.run(debug=True, port=4000)
"""