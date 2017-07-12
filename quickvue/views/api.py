from flask import Blueprint, jsonify
from flask_security import login_required, current_user
import quickvue.api as api


api_blueprint = Blueprint('api_blueprint', __name__,
                  template_folder='templates',
                  static_folder='static')


@api_blueprint.route('/')
def index():
    return jsonify('hello')

@api_blueprint.route('/user')
@login_required
def user():
    user_id = current_user.get_id()
    return jsonify(api.get_user_info(user_id))

