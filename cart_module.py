import database_connection
from flask import Flask,request,jsonify


app=Flask(__name__)
app.config['DEBUG']=True

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
    return "successfully quantity added",200

@app.route('/cart/delete',methods=['DELETE'])
def delete_item():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    db.execute("delete from carts where user_cart_id={} and item_id='{}';".format(user_id, item_id))
    return "Item deleted successfully",200

@app.route('/cart',methods=['GET'])
def fetch_cart_items():
    item=[]
    user_id = request.form['user_id']
    cart_items=db.execute("select items.id,items.name,carts.quantity from items inner join carts on items.id=carts.item_id "
                          "inner join cart_id_holders on cart_id_holders.cart_id=carts.user_cart_id where cart_id_holders.user_id={} ;".format(user_id))
    for row in cart_items:
        item.append("id:{} name:{} quantity:{}".format(row[0],row[1],row[2]))
    return jsonify(item),200

db= database_connection.connect_db()
if __name__ == "__main__":
    app.run()