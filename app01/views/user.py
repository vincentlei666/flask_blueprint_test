from flask import Blueprint, jsonify

user_bluepint = Blueprint("user", __name__)


@user_bluepint.route("/user", methods=["GET", ])
def user():
    return jsonify("用户界面")
