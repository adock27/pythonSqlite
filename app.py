from flask import Flask,jsonify, request
from model import db, Sitios
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\sitios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# tunel de conexion a base de datos 
db.init_app(app)

# ruta root 
@app.route("/")
def home():
    return "<p>Hello, World!</p>"


@app.route("/api/sitios", methods=["GET"])
def getSitios():

    try:
        sitios = Sitios.query.all()
        lista = [sitio.serialize() for sitio in sitios]
        return jsonify(lista), 200
    except Exception:
        print("[SERVER]: Error")
        return jsonify({"mensaje": "Error"}),500
    
    
@app.route("/api/sitio", methods=["GET"])
def getSitioByNombre():

    try:
        name = request.args["name"]
        nombre = Sitios.query.filter_by(nombre=name).first()
        if not nombre:
            return jsonify({"mensaje": "No existe"}),200
        else:
            return jsonify(nombre.serialize()),200
    except Exception:
        print("[SERVER]: Error")
        return jsonify({"mensaje": "Error"}),500


@app.route("/api/buscarSitio", methods=["GET"])
def findSitio():

    try:
        fields = {}
        if "name" in request.args:
            fields["name"] = request.args["name"]
        if "url" in request.args:
            fields["url"] = request.args["url"]
 
        sitio = Sitios.query.filter_by(**fields).first()
        if not sitio:
            return jsonify({"mensaje": "No existe"}),200
        else:
            return jsonify(sitio.serialize()),200
    except Exception:
        print("[SERVER]: Error")
        return jsonify({"mensaje": "Error"}),500

if __name__ == "__main__":
    app.run(debug=True, port=5000)