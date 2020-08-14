from flask import  Flask
from login import login_blueprint
from category import category_blueprint
from cart import cart_blueprint
from logout import logout_blueprint

app=Flask(__name__)
app.secret_key="python flsak project"
app.config['DEBUG']=True

app.register_blueprint(login_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(cart_blueprint)
app.register_blueprint(logout_blueprint)


if __name__ == "__main__":
    app.run()
