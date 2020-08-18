from flask import Flask,request,make_response,jsonify
import jwt
import datetime
from functools import wraps

app=Flask(__name__)
app.config['SECRET KEY']='thisis'
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.args.get('token')
        if not token:
            return jsonify({'message':'token missing'}),403
        try:
            data=jwt.decode(token,app.config['SECRET KEY'])
        except:
            return jsonify({'message':'token is invalid'}),403
        return f(*args,**kwargs)
    return decorated

@app.route('/unprotected')
def unproteced():
    return jsonify({'message':'anyone can view this'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message':'this is available for valid token'})
@app.route('/login')
def login():
    username=request.form['username']
    password=request.form['password']
    if password=='secret':
         token=jwt.encode({'user':username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},app.config['SECRET KEY'])
         return jsonify({'token':token.decode('UTF-8')})
    return make_response('could not verify',401,{'WWW-Authentication':'Basic realm "login required"'})
if __name__=="__main__":
    app.run(debug=True)