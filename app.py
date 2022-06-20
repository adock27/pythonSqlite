from flask import Flask, escape,jsonify, redirect, render_template, request
from requests import delete
from model import db, Sitios
from logging import exception

from web_checker import url_checker

# SQLAlchemy es un Object-Relational Mapper /
# Mapping-tool, o un ORM, es decir una librería que los 
# desarrolladores utilizan para crear bases de datos y 
# manipular sus datos sin la necesidad de conocer / usar SQL.


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\sitios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# tunel de conexion a base de datos 
db.init_app(app)

# ruta root 
@app.route("/")
def home():
    return render_template('index.html')

# ruta de lista de los sitios 
@app.route("/sitios", methods=["GET"])
def getSitios():
    try:
        sitios = Sitios.query.all()
        lista = [sitio.serialize() for sitio in sitios]
        return jsonify(lista), 200
    except Exception:
        print("[SERVER]: Error")
        return jsonify({"mensaje": "Error"}),500

# redireccionar sin id 
@app.route('/sitios/')
def sitios():
    return redirect("/sitios", code=302)


# redireccionar sin id 
@app.route('/sitios/status')
def sitiosStatus():

    try:
        sitios = Sitios.query.all()

        lista = []
        for item in sitios:
            lista.append({
                "nombre": item.nombre,
                "url": item.url,
                "estado": url_checker(item.url),
            })

        return jsonify(lista), 200
            
    except Exception:
        print("[SERVER]: Error")
        return jsonify({"mensaje": "Error"}),500



# obtener por nombre 
@app.route("/sitios/<name>")
def getSiteByName(name):

    name = f"{escape(name)}"

    try:
        nombre = Sitios.query.filter_by(nombre=name).first()
        if not nombre:
            return jsonify({"mensaje": str(name)+" no existe"}),200
        else:
            return jsonify(nombre.serialize()),200
    except Exception:
        print("[SERVER]: Error")
        
        return jsonify({"mensaje": "Error"}),500


# guardar 
@app.route('/sitios/save', methods=['POST'])
def sitioSave():

    try:
            nombre = request.form['nombre']
            url = request.form['url']

            sitio = Sitios(str(nombre),str(url))

            db.session.add(sitio)
            db.session.commit()

            return jsonify(sitio.serialize()), 200
    except Exception as e:
            print("Failed to add book")
            print(e)
    
    return 'success'


# delete by id 
@app.route("/sitios/delete/")
def deleteRedirect():
    return redirect("/", code=302)


# delete by id 
@app.route("/sitios/delete/<id>")
def deleteById(id):

    id = f"{escape(id)}"
    sitio = Sitios.query.get(id)
    db.session.delete(sitio)
    db.session.commit()
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=False, port=5000)