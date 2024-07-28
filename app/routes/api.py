# src/routes/app.py
import sys
import os
from flask import Flask , jsonify , request , Blueprint, redirect , url_for , flash ,render_template
from app.controller import controllerDB
import sqlite3 as sql
from app.routes import routes
#app = Flask(__name__)
api_scope = Blueprint("api", __name__)

# Añadir la carpeta project_root/src al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# sirve para comunicarse con un .py que servia como base de datos
#from app.database.DateToReserve import DateToReserve

db_path = os.path.join("app", "database", "Restaurant.db")

#setting sesion
#esta en config.py y se inicializa en __init__.py

def format():
    conn = sql.connect(db_path)
    dbList = controllerDB.readRow()
   # Convertir las tuplas a diccionarios con claves específicas
    formattedDB = [{'ID': id,'date': date, 'table available': tables } for id,date,tables in dbList]
    conn.close()
    return formattedDB


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
    if request.method == 'POST':
        print(request.form["date"])
        #print(format())
        Exists = False
        for date in format():
            #if date['date'] == request.json['date']:
            if date['date'] == request.form['date']:
                Exists = True
                break
        
        if(not Exists):

            #controllerDB.insertRow(request.json["date"],request.json["table available"])
            controllerDB.insertRow(request.form["date"],request.form["table available"])

            #return jsonify({'message': "Reservetion added sucessfully", "Reserve":format()})
            #return 'Reservetion added sucessfully'
            flash('Reservetion added sucessfully')
            return redirect(url_for('views.home'))
        else:
            #return jsonify({'message': 'This reservation has already created'})
            flash('ERROR : This reservation has already created')
            return redirect(url_for('views.home'))

        
    
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
#Actualiza las reservaciones por medio de la fecha
@api_scope.route ('/edit/<string:DateToReserve_date>', methods = ['PUT'])
def editReservation (DateToReserve_date):
    DateToReserveFound = [ reserve for reserve in format() if reserve['date'] == DateToReserve_date ]

    if (len(DateToReserveFound) > 0):
        Exists = False
        for date in format():
            #if date.get('date') == request.json['date']:
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
    
 #Metodo GET pare editar en html no acepta otros metodos que no sean GET
@api_scope.route ('/edit/<string:DateToReserve_date>')
def editReservation2 (DateToReserve_date):
    DataFound = controllerDB.searchForDate(DateToReserve_date)
    print(DataFound[0])
    return render_template('edit_reservation.html', reservation = DataFound[0])

# crea la nueva reservacion despues de haber sido editada
@api_scope.route('/update/<ID>' , methods = ['POST'])
def update_reservation(ID):
    if request.method == 'POST':
        Exists = False

        for date in format():
            if date['date'] == request.form['date'] and str(date['ID']) != str(ID):
                Exists = True
                break
        
        if(not Exists):
            controllerDB.updateForID(request.form["date"],request.form["table available"],ID)
            flash('Reservetion added sucessfully')
            return redirect(url_for('views.home'))
        else:
            flash('ERROR : This date reservation has already created')
            return redirect(url_for('views.home'))


# Elimina las reservaciones por medio de la fecha 
@api_scope.route('/delete/<string:DateToReserve_date>', methods = ['DELETE'])
def deleteReserve (DateToReserve_date):
    DateToReserveFound =[ reserve for reserve in format() if reserve['date'] == DateToReserve_date]
    if(len(DateToReserveFound) > 0):
        controllerDB.deleteRowForDate(DateToReserve_date)
        #DateToReserve.remove(DateToReserveFound)
        #return jsonify ({'message': 'Reserve Deleted', 'Reserve': format()})
        return routes.home()
    else:    
        #return jsonify ({'message': 'Reserve not found'})
        return 'Reservation not found'

#es un metodo get, porque el home.html y en general los html no reciben metodos que no sean GET
@api_scope.route('/delete/<string:DateToReserve_date>')
def deleteReservetion (DateToReserve_date):
    DateToReserveFound =[ reserve for reserve in format() if reserve['date'] == DateToReserve_date]
    if(len(DateToReserveFound) > 0):
        controllerDB.deleteRowForDate(DateToReserve_date)
        #DateToReserve.remove(DateToReserveFound)
        #return jsonify ({'message': 'Reserve Deleted', 'Reserve': format()})
        flash('Reservetion deleted sucessfully')
        return redirect(url_for('views.home'))
    else:    
        #return jsonify ({'message': 'Reserve not found'})
        return 'Reservation not found'

"""
if __name__ == '__main__':
    app.run(debug=True, port=4000)
"""