from database import connect_db
from flask import Flask,request,jsonify,session,make_response,render_template,redirect,url_for,json
from flask import Blueprint
from models import User
import jwt
import datetime
from functools import wraps
import os
session=connect_db()

login_blueprint=Blueprint('login_blueprint',__name__)


def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.args.get('token')
        if not token:
            return jsonify({'message':'token missing'}),403
        try:
            data = jwt.decode(token,os.environ.get('SECRET_KEY'))
        except:
            return jsonify({'message': 'token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated

@login_blueprint.route('/')
def home():
    return render_template('homepage.html')

@login_blueprint.route('/home',methods=['GET'])
def home_page():
    a="welcome to online shopping"
    return jsonify(a),200

@login_blueprint.route('/login')
def sinup():
    return render_template('login.html')

@login_blueprint.route('/login',methods=['POST'])
def login():
    user_name=request.form['username']
    password=request.form['password']
    try:
        user_info=session.query(User.id).filter_by(name=user_name,password=password).first()
        if user_info:
            a=user_info[0]
            token = jwt.encode({'user': user_name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)},os.environ.get('SECRET_KEY'))
            encode_token=token.decode('UTF-8')
            return render_template('category.html',a=a)
        return render_template('login.html'),401
    except Exception as e:
        return (str(e))

