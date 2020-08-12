from flask import Flask,request,jsonify
from sqlalchemy import create_engine

app=Flask(__name__)
app.config['DEBUG']=True

def connect_db():
    connection_string="postgresql://postgres:7538821247@localhost:5432/shopping"
    return create_engine(connection_string)

@app.route('/')
def home_page():
    return "WELCOME  TO   ONLINE   SHOPPING",200

@app.route('/categories',methods=['GET'])
def fetch_categories():
    category_list = db.execute("select * from categories")
    category=[dict(row) for row in category_list]
    return jsonify(category),200

@app.route('/categories/<category_id>' ,methods=['GET'])
def fetch_items(category_id):
    formated_items=[]
    item_list = db.execute("select items.name,items.price ,sellers.name ,sellers.phone_no from "
                           "((items inner join categories on items.category_id=categories.id) "
                           "inner join sellers on items.seller_id=sellers.id) where categories.id='{}';".format(category_id))
    for res in item_list:
        formated_items.append ("name:{} price:{} sellername:{} phoneno:{}".format(res[0],res[1],res[2],res[3]))
    return jsonify(formated_items)


@app.route('/cart/add',methods=['POST'])
def add_cart():
    user_id=request.form['user_id']
    item_id=request.form['item_id']
    db.execute("insert into carts(user_cart_id,item_id) values({},'{}');".format(user_id,item_id))
    return "Item added successfully ",200

@app.route('/cart/quantity',methods=['PUT'])
def modify_quantity():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    quantity=request.form['quantity']
    db.execute("update carts set quantity={} where user_cart_id={} and item_id={};".format(quantity,user_id,item_id))
    return "successfully modified",200

@app.route('/cart/delete',methods=['DELETE'])
def delete_item():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    db.execute("delete from carts where user_cart_id={} and item_id='{}';".format(user_id, item_id))
    return "Item deleted successfully",200

@app.route('/cart',methods=['GET'])
def fetch_cart_items():
    user_id = request.form['user_id']
    cart_items=db.execute("select items.name from items inner join carts on items.id=carts.item_id "
                          "inner join cart_id_holders on cart_id_holders.cart_id=carts.user_cart_id where cart_id_holders.user_id={} ;".format(user_id))
    item=[str(row[0]) for row in cart_items]
    return jsonify(item),200

db=connect_db()
if __name__ == "__main__":
    app.run()
