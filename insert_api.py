#API CON CONEXION POSGRESS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask("__name_")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://hoangnd:joel@localhost:5432/1222'
db = SQLAlchemy(app)

class Person(db.Model):
    IdUsuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(120), unique=False)
    Apellido = db.Column(db.String(120), unique=False)
    Correo = db.Column(db.String(220), unique=False)

    def __init__(self, Nombre, Apellido, Correo):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Correo = Correo

@app.route('/insert_user', methods=['POST'])
def insertUser():
    newFirstName = request.form['first_name']
    newLastName = request.form['last_name']
    newEmail = request.form['email']
    user = Person(newFirstName, newLastName, newEmail)
    db.session.add(user)
    db.session.commit()
    return "<p>Data is updated</p>"

if __name__ == '__main__':
    app.run()
