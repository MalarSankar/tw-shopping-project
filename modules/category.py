from database import connect_db
from flask import Flask,request,jsonify,session,render_template,redirect
from flask import Blueprint
from models import Category,Item,Seller
session=connect_db()

category_blueprint=Blueprint('category_bluprint',__name__)

@category_blueprint.route('/category',methods=['GET'])
def category():
    return render_template('category.html'),200

@category_blueprint.route('/categories',methods=['GET'])
def fetch_categories():
        try:
            result_list=[]
            category_list = session.execute("select * from categories;")
            result_list=[dict(row) for row in category_list ]
            return jsonify(result_list),200
        except Exception as e:
            return (str(e))

@category_blueprint.route('/categories/<category_id>' ,methods=['GET'])
def fetch_items(category_id):
    try:
        item_list = session.query(Item.id, Item.name).filter(Item.category_id == category_id).all()
        item_list=[{"id":int(res[0]),"name":str(res[1])} for res in item_list]
        return jsonify(item_list),200
    except Exception as e:
        return (str(e))

@category_blueprint.route('/item/<item_id>',methods=['GET'])
def particular_item(item_id):
    try:
        item=session.query(Item.id,Item.price,Seller.name, Seller.phone_no).filter(Item.id ==item_id).filter(Item.seller_id == Seller.id).all()
        item=[{"id":int(res[0]),"price":float(res[1]),"sellername":str(res[2]),"seller_no":int(res[3])} for res in item]
        return jsonify(item),200
    except Exception as e:
        return (str(e))

