from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:stefan@localhost/employee'
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app,db)
migrate.init_app(app, db)

# Det vi gör är  CODE-FIRST !!!!
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    birthdate = db.Column(db.Date)
    city = db.Column(db.String(40), unique=False, nullable=False)
    shoesize = db.Column(db.Integer, unique=False, nullable=False)
   #inloggningstimestamp = db.Column(db.DateTime)

def Search():
    txt = input("Ange text att söka på:")
    result = Employee.query.filter(Employee.namn.contains(txt)).all() 
    for emp in result:
        print(f"{emp.id} {emp.namn}")
    sel = int(input("Ange id på en som du vill uppdatera eller 0"))
    if sel == 0:
        return
    employee = Employee.query.filter_by(id = sel).first()
    employee.namn = input("Ange nytt namn")
    employee.age = int(input("Ange ny age"))
    employee.city = input("Ange ny city:")
    employee.shoesize = int(input("Ange ny shoesize"))
    db.session.commit()
        



def CreateNew():
    b = Employee()
    b.namn = input("Ange namn:")
    b.age = int(input("Ange age:"))
    b.city = input("Ange city:")
    b.shoesize = int(input("Ange shoesize"))
    # TODO ska fixa birthdate strax - strptime
    db.session.add(b)
    db.session.commit() 

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        #db.create_all()
        #upgrade()

        while True:
            print("1. Sök ")
            print("2. Skapa ny ")
            action = input("Ange val:")
            if action == "2":
                CreateNew()
            if action == "1":
                Search()

