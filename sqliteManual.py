# importar sqllite3 
import sqlite3 as sql


def createDB():
    conn = sql.connect("sitios.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE sitios (
        nombre text,
        url text
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre,url):
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"INSERT INTO sitios VALUES ('{nombre}','{url}')"
    cursor.execute(query)
    conn.commit()
    conn.close()

def insertRows(list):
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"INSERT INTO sitios VALUES ( ?, ? )"
    cursor.executemany(query,list)
    conn.commit()
    conn.close()


def readRows():
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM sitios"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)


def readOrderBy(field):
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM sitios ORDER BY {field}"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)


def readOrderByDesc(field):
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM sitios ORDER BY {field} DESC"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)

def search(nombre):
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM sitios WHERE nombre like '%{nombre}%'"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)


def update(nombre,url):
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"UPDATE sitios SET url = '{url}' WHERE nombre like '{nombre}'"
    cursor.execute(query)
    conn.commit()
    conn.close()

def delete(nombre):
    conn = sql.connect("sitios.db")
    cursor = conn.cursor()
    query = f"DELETE FROM sitios WHERE nombre = '{nombre}'"
    cursor.execute(query)
    conn.commit()
    conn.close()

# inicializador de archivo puthon 
# if __name__ == "__main__":
    # createDB()
    # createTable()
    # insertRow("Google","www.google.com")
    # readRow()

    sitios = [
        ("cartagena","cartagena.gov.co"),
        ("mipg","mipg.cartagena.gov.co"),
        ("odus","odus.cartagena.gov.co")
    ]

    # insertRows(sitios)


    # readRows()
    # readOrderBy("name")
    # readOrderByDesc("url")

    # search("gena")
    # update("cartagena","www.cartagena.gov.co")
    # delete("Google")
    # readRows()