from flask import jsonify, Blueprint

order_blueprint = Blueprint("order", __name__)


@order_blueprint.route("/order", methods=["GET", ])
def order():
    return jsonify("订单页面")
