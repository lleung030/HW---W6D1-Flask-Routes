from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(50), unique = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(200))
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    title = db.Column(db.String(250), nullable = False)   
    body = db.Column(db.String(250), nullable = False)   
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    make = db.Column(db.String(250), nullable = False)
    model = db.Column(db.String(250), nullable = False)
    year = db.Column(db.Integer, nullable = False)   
    color = db.Column(db.String(250), nullable = False)
    price = db.Column(db.Float, nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    