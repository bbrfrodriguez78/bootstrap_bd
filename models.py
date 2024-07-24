from bootstrapg2bd import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    comentario = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(8), nullable=False)