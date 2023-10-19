from flask import Flask
from .user import user_bluepint
from .order import order_bluepint

app = Flask(__name__)

app.register_blueprint(user_bluepint)
app.register_blueprint(order_bluepint)







