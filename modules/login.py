import database
from flask import Flask,request,jsonify,session
from flask import Blueprint

login_blueprint=Blueprint('login_blueprint',__name__)

@login_blueprint.route('/',methods=['GET'])
def home_page():
    return "WELCOME  TO   ONLINE   SHOPPING",200

@login_blueprint.route('/login',methods=['POST'])
def login():
    user_name=request.form['user_name']
    password=request.form['password']
    try:
        user_info=db.execute("select id from users where name='{}' and password='{}';".format(user_name,password))
        user_info = [str(row[0]) for row in user_info]
        if len(user_info) == 1:
            session['user']=user_name
            return jsonify("authorized user"), 200
    
        return jsonify("unauthorized user"), 401
    except Exception as e:
        return (str(e))

db= database.connect_db()
