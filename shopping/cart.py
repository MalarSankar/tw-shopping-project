import database
from flask import Flask,request,jsonify,session
from flask import Blueprint

cart_blueprint=Blueprint('cart_blueprint',__name__)


@cart_blueprint.route('/cart/add',methods=['POST'])
def add_cart():
    user_id=request.form['user_id']
    item_id=request.form['item_id']
    if "user" in session:
        db.execute("insert into carts(user_id,item_id) values({},'{}');".format(user_id,item_id))
        return "Item added successfully ",200
    else:
        return "unauthorized user",401

@cart_blueprint.route('/cart/quantity',methods=['PUT'])
def modify_quantity():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    quantity=request.form['quantity']
    if "user" in session==user_id:
        db.execute("update carts set quantity={} where user_id={} and item_id={};".format(quantity,user_id,item_id))
        return "successfully quantity added",200
    else:
        return "unauthorized user",401

@cart_blueprint.route('/cart/delete',methods=['DELETE'])
def delete_item():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    if "user" in session:
        db.execute("delete from carts where user_id={} and item_id='{}';".format(user_id, item_id))
        return "Item deleted successfully",200
    else:
        return "unauthorized user",401

@cart_blueprint.route('/cart',methods=['GET'])
def fetch_cart_items():
    item=[]
    user_id = request.form['user_id']
    if "user" in session:
        cart_items=db.execute("select items.name,carts.quantity from carts inner join items on items.id=carts.item_id where carts.user_id={} ;".format(user_id))
        for row in cart_items:
            item.append("item:{} quantity:{}".format(row[0],row[1]))
        return jsonify(item),200
    else:
        return "unauthorized user",401

db= database.connect_db()
