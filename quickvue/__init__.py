from flask import Flask, make_response, jsonify
from http import HTTPStatus
from flask_security import Security, PeeweeUserDatastore
from playhouse.flask_utils import FlaskDB
import config.config as config

app = Flask(__name__)
app.config.from_object(config.config)

db_wrapper = FlaskDB(app)
db = db_wrapper.database

from quickvue.core.models import User, Role, UserRoles
user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

# Register blueprints
from quickvue.views import home, api_blueprint
app.register_blueprint(home)
app.register_blueprint(api_blueprint, url_prefix='/api')


@app.errorhandler(HTTPStatus.UNAUTHORIZED)
def unauthorized(error):
    return make_response(jsonify({'error': error.description}), error.code)
