from flask import Flask,request,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app=Flask(__name__)
app.config['DEBUG']=True

def connect_db():
    connection_string="postgresql://postgres:7538821247@localhost:5432/shopping"
    return create_engine(connection_string)

@app.route('/')
def home_page():
    return "WELCOME  TO   ONLINE   SHOPPING"

@app.route('/login',methods=['POST'])
def login():
    value = "invalid user"
    user_name = request.form['user_name']
    password = request.form['password']
    password_list = db.execute("select * from users where password='{}' and name='{}'".format(password, user_name))
    for row in password_list:
        value = "welcome" + " " + str(row.name)
    return jsonify(value)

def category_format(row):
    return   str(row.id) +  ": " + str(row.name)

@app.route('/categories',methods=['GET'])
def fetch_categories():
        category_list = db.execute("select * from categories")
        category= [category_format(row) for row in category_list]
        return jsonify(category)

@app.route('/categories/<category_id>' ,methods=['GET'])
def fetch_items(category_id):
    formated_item_list=[]
    item_list = db.execute("select items.name,items.price ,sellers.name,sellers.phone_no from "
                           "((items inner join categories on items.category_id=categories.id) "
                           "inner join sellers on items.seller_id=sellers.id) where categories.id='{}';".format(category_id))
    for row in item_list:
        formated_item_list.append("name:"+str(row[0])+"  "+"price:"+str(row[1])+"  "+"seller name:"+str(row[2])+"  "+"seller phone_no:"+str(row[3]))
    return jsonify(formated_item_list)

@app.route('/cart/add',methods=['POST'])
def add_cart():
    user_id=request.form['user_id']
    item=request.form['item']
    db.execute("insert into carts(user_cart_id,item) values({},'{}');".format(user_id,item))
    return "Item added successfully "


@app.route('/cart/delete',methods=['DELETE'])
def delete_item():
    user_id = request.form['user_id']
    item = request.form['item']
    db.execute("delete from carts where user_cart_id={} and item='{}';".format(user_id, item))
    return "Item deleted successfully"

@app.route('/view cart',methods=['GET'])
def fetch_cart_items():
    user_id = request.form['user_id']
    cart_items=db.execute("select item from carts where user_cart_id={} ;".format(user_id))
    item=[str(row.item) for row in cart_items]
    return jsonify(item)
db=connect_db()
if __name__ == "__main__":
    app.run()
