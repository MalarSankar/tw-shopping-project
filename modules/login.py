from database import connect_db
from flask import Flask,request,jsonify,session
from flask import Blueprint
from models import User
session=connect_db()

login_blueprint=Blueprint('login_blueprint',__name__)
@login_blueprint.route('/',methods=['GET'])
def home_page():
    return "WELCOME  TO   ONLINE   SHOPPING",200

@login_blueprint.route('/login',methods=['POST'])
def login():
    user_name=request.form['user_name']
    password=request.form['password']
    try:
        user_info=session.query(User.id).filter_by(name=user_name,password=password).first()
        if user_info:
            session['user']=user_name
            return "authorized user",200
        return "unauthorized user",401
    except Exception as e:
        return (str(e))

