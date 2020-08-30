from flask import  Flask
from login import login_blueprint
from category import category_blueprint
from cart import cart_blueprint
from logout import logout_blueprint
import os

app=Flask(__name__,template_folder='template')

app.config['DEBUG']=True
app.config['SECRET KEY']=os.environ.get('SECRET_KEY')

app.register_blueprint(login_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(cart_blueprint)
app.register_blueprint(logout_blueprint)

if __name__ == "__main__":
    app.run(host="localhost",port=8000)
