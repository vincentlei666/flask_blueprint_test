from flask import jsonify, Blueprint

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/user", methods=["GET", ])
def user():
    return jsonify("用户页面")
