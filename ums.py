from flask import Flask, request, jsonify
from flask import Flask, request, render_template, flash, redirect, url_for, session
from flask_cors import CORS
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import time
import datetime
import requests

model = None
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/userSystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class Users(db.Model):
    __tablename__ = "users"

    userID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Integer(), nullable=False) 

    def __init__(self, firstName, lastName, email, dob):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.dob = dob
    
    def json(self):
        return{"id": self.userID, "firstName": self.firstName, "lastName": self.lastName, "email": self.email, "dob": self.dob}


@app.route("/add_users", methods=["POST"])
def add_users():
    if request.method == "POST":
        firstName = request.form['addFirstName'].strip().capitalize()
        lastName = request.form['addLastName'].strip().capitalize()
        email = request.form['addEmail'].strip()
        dobDate = request.form['addDob']

        dob = time.mktime(datetime.datetime.strptime(dobDate, "%Y-%M-%d").timetuple())
        user = Users.query.filter_by(email=email).first()
        if not user:
            add_user = Users(firstName=firstName, lastName=lastName, email=email, dob=dob)
            db.session.add(add_user)
            db.session.commit()
        else: 
            message = jsonify({"message": "User email already existed. Please go back and try again"})
            return message
    return redirect(request.referrer)

@app.route("/update_users", methods=["POST"])
def update_users():
    if request.method == "POST":
        userID = request.form['updateID']
        firstName = request.form['updateFirstName'].strip().capitalize()
        lastName = request.form['updateLastName'].strip().capitalize()
        email = request.form['updateEmail'].strip()
        dobDate = request.form['updateDob']

        dob = time.mktime(datetime.datetime.strptime(dobDate, "%Y-%M-%d").timetuple())

        user = Users.query.filter_by(email=email).first()
        if not user:
            userUpdate = Users.query.filter_by(userID=userID).first()
            userUpdate.firstName = firstName
            userUpdate.lastName = lastName
            userUpdate.email = email
            userUpdate.dob = dob    
            db.session.commit()
        else:
            message = jsonify({"message": "User email already existed. Please go back and try again"})
            return message
    return redirect(request.referrer)    

@app.route("/delete_users/<string:userID>")
def delete_users(userID):
    Users.query.filter_by(userID=userID).delete()
    db.session.commit()
    return redirect(request.referrer)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        all_users = Users.query.all()
    return render_template("index.html", all_users=all_users)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
