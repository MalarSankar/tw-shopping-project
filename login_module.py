import database_connection
from flask import Flask,request,jsonify


app=Flask(__name__)
app.config['DEBUG']=True


@app.route('/')
def home_page():
    return "WELCOME  TO   ONLINE   SHOPPING",200

@app.route('/login',methods=['POST'])
def login():
    user_name=request.form['user_name']
    password=request.form['password']
    user_info=db.execute("select id from users where name='{}' and password='{}';".format(user_name,password))
    user_info=[str(row[0]) for row in user_info]
    if len(user_info)==1:
        return jsonify("authorized user"),200
    else:
        return jsonify("unauthorized user"),401

db= database_connection.connect_db()
if __name__ == "__main__":
    app.run()