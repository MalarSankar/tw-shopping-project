from database import connect_db
from flask import Flask,request,jsonify,session,make_response
from flask import Blueprint
from models import User
import jwt
import datetime
from functools import wraps
session=connect_db()

login_blueprint=Blueprint('login_blueprint',__name__)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.args.get('token')
        if not token:
            return jsonify({'message':'token missing'}),403
        try:
            data = jwt.decode(token,'flask project')
        except:
            return jsonify({'message': 'token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated

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
            token = jwt.encode({'user': user_name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)},'flask project')
            return jsonify({'token': token.decode('UTF-8')})
        return make_response('could not verify', 401, {'WWW-Authentication': 'Basic realm "login required"'})
    except Exception as e:
        return (str(e))

