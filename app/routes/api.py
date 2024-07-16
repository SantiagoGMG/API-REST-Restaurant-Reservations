# src/routes/app.py
import sys
import os
from flask import Flask , jsonify , request , Blueprint
from flask_mysqldb import MySQL

# Añadir la carpeta project_root/src al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.database.DateToReserve import DateToReserve

from app.controller import controllerDB
import sqlite3 as sql

db_path = os.path.join("app", "database", "Restaurant.db")
conn = sql.connect(db_path)

def format():
    dbList = controllerDB.readRow()
   # Convertir las tuplas a diccionarios con claves específicas
    formattedDB = [{'date': date, 'table available': tables , 'ID': id} for date,tables,id in dbList]
    return formattedDB
#app = Flask(__name__)
api_scope = Blueprint("api", __name__)

#TESTER

@api_scope.route('/ping', methods = ['GET'])
def ping():
    return jsonify({'message' : 'pong'})
"""
@api_scope.route('/reserve', methods = ['GET'])
def reserve():
    return jsonify({ 'message': "date available to reserve", "DateToReserve": DateToReserve })
"""
    #controllerDB.readRow() 
#Retorna toda la base de datos en formato json
@api_scope.route('/reserve', methods = ['GET'])
def reserve():
    return jsonify({ 'message': "date available to reserve", "DateToReserve": format() })

#Busca uan fecha en la lista de base de datos y lo devuelve como json
@api_scope.route('/reserve/<string:DateToReserve_date>', methods = ['GET'])
def getReserve(DateToReserve_date):

    DateToReserveFound = [date for date in format() if date['date']==DateToReserve_date]
    if (len(DateToReserveFound) > 0):
        return jsonify({'Date available to reserve '+ DateToReserve_date :DateToReserveFound[0]})
    else:
        return jsonify({'message':'Date unavailable'})
"""
@api_scope.route('/reserve' , methods = ['POST'])
def addReserve():
    for date in DateToReserve:
        if date.get('date') == request.json['date']:
            Exists = True
            break
    
    if(not Exists):
        newReserve = {
            "date": request.json["date"],
            "table available" : request.json["table available"]
        }
        DateToReserve.append(newReserve)
        
        return jsonify({'message': "Reservetion added sucessfully", "Reserve":DateToReserve})
    else:
        return jsonify({'message': 'This reservation has already created'})
"""
# crea reservaciones
@api_scope.route('/reserve' , methods = ['POST'])
def addReserve():
    print(format())
    Exists = False
    for date in format():
        if date['date'] == request.json['date']:
            Exists = True
            break
    
    if(not Exists):
        newReserve = {
            "date": request.json["date"],
            "tableAvailable" : request.json["table available"]
        }
        controllerDB.insertRow(request.json["date"],request.json["table available"])
        
        return jsonify({'message': "Reservetion added sucessfully", "Reserve":format()})
    else:
        return jsonify({'message': 'This reservation has already created'})
    
"""   
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
            return jsonify({'message' : 'Reservetion Updated', 'reservetion':DateToReserveFound[0]})
        else:
            return jsonify('Esa fecha ya existe y no coincide con la fecha que estas actualizando')
    else:
        return jsonify({'message': 'Product not found'})
"""    

@api_scope.route ('/reserve/<string:DateToReserve_date>', methods = ['PUT'])
def editReservation (DateToReserve_date):
    DateToReserveFound = [ reserve for reserve in format() if reserve['date'] == DateToReserve_date ]

    if (len(DateToReserveFound) > 0):
        Exists = False
        for date in format():
            if date.get('date') == request.json['date']:
                Exists = True
                break

        if(not Exists):
            acceder = DateToReserveFound[0]
            id = acceder['ID']
            print(id)
            DateToReserveFound[0]['date'] = request.json['date']
            DateToReserveFound[0]['table available'] = request.json['table available']
            controllerDB.updateForID(request.json['date'],request.json['table available'],id)
            return jsonify({'message' : 'Reservetion Updated', 'reservetion':DateToReserveFound[0]})
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


"""
if __name__ == '__main__':
    app.run(debug=True, port=4000)
"""