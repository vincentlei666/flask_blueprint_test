from flask import Flask

from .order import order_blueprint
from .user import user_blueprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(user_blueprint)
app.register_blueprint(order_blueprint)
