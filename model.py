from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Sitios(db.Model):
    rowid = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(200), unique= True,nullable = False)
    url = db.Column(db.String(512))

    def __init__(self, nombre, url):
        self.nombre = nombre
        self.url = url

    def __str__(self):
        return "Nombre: {} Url: {}".format(
            self.nombre,
            self.url
        )
    
    def serialize(self):
        return{
            "rowid": self.rowid,
            "nombre": self.nombre,
            "url": self.url,
        }
    