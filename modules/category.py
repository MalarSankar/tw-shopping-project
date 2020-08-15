import database
from flask import Flask,request,jsonify,session
from flask import Blueprint

category_blueprint=Blueprint('category_bluprint',__name__)

@category_blueprint.route('/categories',methods=['GET'])
def fetch_categories():
    if "user" in session:
        category_list = db.execute("select * from categories")
        category=[dict(row) for row in category_list]
        return jsonify(category),200
    return "unauthorized user",401

@category_blueprint.route('/categories/<category_id>' ,methods=['GET'])
def fetch_items(category_id):
    formated_items=[]
    if "user" in session:
        item_list = db.execute("select items.id, items.name,items.price ,sellers.name ,sellers.phone_no from "
                           "((items inner join categories on items.category_id=categories.id) "
                           "inner join sellers on items.seller_id=sellers.id) where categories.id='{}';".format(category_id))
        for res in item_list:
            formated_items.append ("id:{} name:{} price:{} sellername:{} phoneno:{}".format(res[0],res[1],res[2],res[3],res[4]))
        return jsonify(formated_items),200
    return "unauthorized user",401


db= database.connect_db()
