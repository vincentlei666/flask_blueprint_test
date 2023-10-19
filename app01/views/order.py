from flask import Blueprint, jsonify

order_bluepint = Blueprint("order", __name__)


@order_bluepint.route("/order", methods=["GET", ])
def order():
    return jsonify("订单界面")
