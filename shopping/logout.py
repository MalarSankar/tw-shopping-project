from flask import Flask,request,jsonify,session
from flask import Blueprint

logout_blueprint=Blueprint("logout_blueprint",__name__)

@logout_blueprint.route('/logout')
def logout():
    if 'user' in session:
        session.pop("user", None)
        return ("logged out"), 200
    else:
        return "please login",200