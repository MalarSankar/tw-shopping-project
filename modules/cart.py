from database import connect_db
from flask import Flask,request,jsonify,session
from flask import Blueprint
from models import Cart,Item
session=connect_db()

cart_blueprint=Blueprint('cart_blueprint',__name__)

@cart_blueprint.route('/cart',methods=['POST'])
def add_cart():
    user_id=request.form['user_id']
    item_id=request.form['item_id']
    if "user" in session:
        try:
            cart_info=Cart(user_id=user_id,item_id=item_id,quantity=1)
            session.add(cart_info)
            session.commit()
            return "Item added successfully ",200
        except Exception as e:
            return str(e)
    return "unauthorized user", 401


@cart_blueprint.route('/cart',methods=['PUT'])
def modify_quantity():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    quantity=request.form['quantity']
    if "user" in session:
        try:
            cart_info=session.query(Cart).filter_by(user_id=user_id,item_id=item_id).first()
            cart_info.quantity=quantity
            session.commit()
            return "successfully quantity updated",200
        except Exception as e:
            return str(e)
    return "unauthorized user", 401


@cart_blueprint.route('/cart',methods=['DELETE'])
def delete_item():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    if "user" in session:
        try:
            cart_info=session.query(Cart).filter_by(user_id=user_id,item_id=item_id).first()
            session.delete(cart_info)
            session.commit()
            return "successfully deleted",200
        except Exception as e:
            return str(e)
    return "unauthorized user", 401


@cart_blueprint.route('/cart',methods=['GET'])
def fetch_cart_items():
    item=[]
    user_id = request.form['user_id']
    if "user" in session:
        try:
            cart_items=session.query(Item.name,Cart.quantity).filter(Cart.item_id==Item.id).filter(Cart.user_id==user_id).all()
            for row in cart_items :
                item.append("item:{} quantity:{}".format(row[0],row[1]))
            return jsonify(item),200
        except Exception as e:
            return str(e)
    return "unauthorized user",401



