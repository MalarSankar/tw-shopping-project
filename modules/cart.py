from database import connect_db
from flask import Flask,request,jsonify,session,render_template
from flask import Blueprint
from models import Cart,Item
session=connect_db()

cart_blueprint=Blueprint('cart_blueprint',__name__)

@cart_blueprint.route('/acart',methods=['POST'])
def add_cart():
    user_id=request.form['user_id']
    item_id=request.form['item_id']
    try:
        cart_info=Cart(user_id=user_id,item_id=item_id,quantity=1)
        session.add(cart_info)
        session.commit()
        return "Item added successfully ",200
    except Exception as e:
        return str(e)


@cart_blueprint.route('/cart',methods=['PUT'])
def modify_quantity():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    quantity=request.form['quantity']
    try:
        cart_info=session.query(Cart).filter_by(user_id=user_id,item_id=item_id).first()
        cart_info.quantity=quantity
        session.commit()
        return "successfully quantity updated",200
    except Exception as e:
        return str(e)

@cart_blueprint.route('/modify')
def modify():
    return render_template('modifycart.html'),200

@cart_blueprint.route('/cart',methods=['DELETE'])
def delete_item():
    user_id = request.form['user_id']
    item_id = request.form['item_id']
    try:
        cart_info=session.query(Cart).filter_by(user_id=user_id,item_id=item_id).first()
        session.delete(cart_info)
        session.commit()
        return "successfully deleted",200
    except Exception as e:
        return str(e)

@cart_blueprint.route('/addcart')
def addcart():
    return render_template('additem.html'),200

@cart_blueprint.route('/cart1')
def cart():
    return render_template('viewcart.html'),200

@cart_blueprint.route('/cart',methods=['POST'])
def fetch_cart_items():
    item=[]
    user_id = request.form['user_id']
    try:
        cart_items=session.query(Item.id,Item.name,Cart.quantity).filter(Cart.item_id==Item.id).filter(Cart.user_id==user_id).all()
        cart_items = [{"id": int(row[0]), "name": str(row[1]), "quantity": int(row[2])} for row in cart_items]
        return jsonify(cart_items), 200
    except Exception as e:
        return str(e)




