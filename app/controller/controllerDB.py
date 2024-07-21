import sqlite3 as sql
import os

def createDB():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    conn.commit()
    conn.close()

def createTable():
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE dateToReserve
                (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  date DATE,
                  tableAvailable INTEGER
                ) """
                   )
    conn.commit()
    conn.close()

def insertRow(date, tableAvailable):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO dateToReserve (date, tableAvailable) VALUES('{date}', {tableAvailable})"
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
    instruccion = f"INSERT INTO dateToReserve (date, tableAvailable) VALUES(?,?)"
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

def updateTables(date, tableAvailable):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"UPDATE dateToReserve SET tableAvailable = {tableAvailable} WHERE date = '{date}'"
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

def updateForID (updateDate, updateTable, ID):
    db_path = os.path.join("app", "database", "Restaurant.db")
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruccion = f"UPDATE dateToReserve SET date = '{updateDate}',tableAvailable = {updateTable} WHERE ID = {ID}"
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


if __name__ == "__main__":
    createDB()
    createTable()
    insertRow('2025-01-01',22)
    insertRow('2025-01-02',10)
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
    readRow()
