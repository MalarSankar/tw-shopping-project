from database import connect_db
from flask import Flask,request,jsonify,session
from flask import Blueprint
from models import Category,Item,Seller
session=connect_db()


category_blueprint=Blueprint('category_bluprint',__name__)

@category_blueprint.route('/categories',methods=['GET'])
def fetch_categories():
    if "user" in session:
        try:
            result_list=[]
            category_list = session.query(Category).all()
            for res in category_list:
                result_list.append("id:{}   name:{}".format(res.id,res.name))
            return jsonify(result_list),200
        except Exception as e:
            return (str(e))
    return "unauthorized user", 401

@category_blueprint.route('/categories/<category_id>' ,methods=['GET'])
def fetch_items(category_id):
    formated_items=[]
    if "user" in session:
        try:
            item_list = session.query(Item.id,Item.name,Item.price,Seller.name,Seller.phone_no).filter(Item.category_id==category_id).filter(Item.seller_id==Seller.id).all()
            for res in item_list:
                formated_items.append ("id:{} name:{} price:{} sellername:{} phone_no:{} ".format(res[0],res[1],res[2],res[3],res[4]))
            return jsonify(formated_items),200
        except Exception as e:
            return (str(e))
    return "unauthorized user", 401



