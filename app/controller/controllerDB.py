import sqlite3 as sql
import os


def insertRow(date, number_of_tables):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO dateToReserve (date, number_of_tables) VALUES('{date}', {number_of_tables})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRow():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM dateToReserve "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    #print(datos)
    return datos

def insertRows(reservationList):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO dateToReserve (date, number_of_tables) VALUES(?,?)"
    cursor.executemany(instruccion,reservationList)
    conn.commit()
    conn.close()

def readOrdered (field):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM dateToReserve ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def searchForDate(date):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM dateToReserve WHERE date = '{date}' "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    return datos

def updateTables(date, number_of_tables):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"UPDATE dateToReserve SET number_of_tables = {number_of_tables} WHERE date = '{date}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def updateDate (newDate, changeDate):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"UPDATE dateToReserve SET date = '{newDate}' WHERE date = '{changeDate}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def updateForID (updateDate, updateTables, ID):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"UPDATE dateToReserve SET date = '{updateDate}',number_of_tables = {updateTables} WHERE ID = {ID}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteRowForDate(deleteDate):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"DELETE  FROM dateToReserve WhERE date = '{deleteDate}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def deleteRowForID(deleteID):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"DELETE  FROM dateToReserve WhERE Id = '{deleteID}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()



"""
def createTable():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        CREATE TABLE dateToReserve
                (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  date DATE,
                  number_of_tables INTEGER
                ) 
                   )
    conn.commit()
    conn.close()
"""

def createDB():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    conn.commit()
    conn.close()

def createTable_Mesas():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Mesas
                (
                ID_Mesa INTEGER PRIMARY KEY AUTOINCREMENT,
                capacidad_maxima INTEGER
                ) """
    )
    conn.commit()
    conn.close()

def deleteRowMesasForID(deleteID):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"DELETE FROM Mesas WhERE ID_Mesa = '{deleteID}'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deleteRowMesasAll():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"DELETE FROM Mesas;"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRowMesas():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Mesas "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos

def readLastRowMesas():
    db_path = os.path.join("app","database","Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Mesas ORDER BY ID_Mesa DESC LIMIT 1"
    cursor.execute(instruccion)
    datos = cursor.fetchone()
    conn.commit()
    conn.close()
    print(datos)
    return datos

def searchForID_Mesas(ID):
    db_path = os.path.join("app","database","Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Mesas WHERE ID_Mesa = '{ID}'"
    cursor.execute(instruccion)
    datos = cursor.fetchone()
    conn.commit()
    conn.close()
    print(datos)
    return datos

def insertRowMesas(number_of_chair):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Mesas (capacidad_maxima) VALUES({number_of_chair})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def updateMesa(ID, new_capacidad):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"UPDATE Mesas SET capacidad_maxima = '{new_capacidad}' WHERE ID_Mesa = '{ID}' "
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

    
def createTable_Disponibilidad():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Disponibilidad
                (
                ID_Disponibilidad INTEGER PRIMARY KEY AUTOINCREMENT,
                ID_Mesa INTEGER,
                Fecha_Reserva DATE,
                Sillas_Disponibles INTEGER,
                Hora TIME,
                Disponible BOOLEAN,
                FOREIGN KEY(ID_Mesa) REFERENCES Mesas(ID_Mesa)
                ) """
    )
    conn.commit()
    conn.close()


def createTable_Usuarios():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Usuarios
                (
                ID_Disponibilidad INTEGER PRIMARY KEY AUTOINCREMENT,
                  ID_Usuarios INTEGER,
                  Nombre VARCHAR(255),
                  Email VARCHAR(255),
                  Telefono VARCHAR(15),
                  Tipo VARCHAR(50)
                  
                ) """
                   )
    conn.commit()
    conn.close()

def createTable_Reservacion():
    db_path = os.path.join("app","database","Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(

        """CREATE TABLE IF NOT EXISTS Reservacion
        (
        ID_Reservaciones INTEGER PRIMARY KEY AUTOINCREMENT,
        Fecha_Reserva DATE,
        Hora TIME,
        ID_Usuario INTEGER,
        ID_Mesa INTEGER,
        FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuarios),
        FOREIGN KEY (ID_Mesa) REFERENCES Mesas(ID_Mesa)
        )
        """
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow('2025-01-01',22)
    #insertRow('2025-01-02',10)
    #readRow()
    reservation = [
        ('2025-01-03',35),
        ('2025-01-04',100)
        ]
    #insertRows(reservation)
    #readOrdered("tableAvailable")
    #searchForDate('2025-01-01')
    #updateTables('2025-01-03',25)
    #updateDate('2025-01-05','2025-01-04')
    #deleteRowForDate('2025-01-04')
    #update8ForID('2025-01-04',2,4)
    #readRow()
    createDB()
    createTable_Mesas()
    createTable_Disponibilidad()
    createTable_Usuarios()
    createTable_Reservacion()
    readRowMesas()
    readLastRowMesas()
