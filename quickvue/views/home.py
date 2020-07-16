from flask import Blueprint, render_template
from flask_security import login_required
from quickvue import db, user_datastore
from quickvue.core.models import User, Role, UserRoles

home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')


@home.route('/')
def index():
    bootstrap = None
    return render_template('index.html', bootstrap=bootstrap)

@home.route('/private')
@login_required
def private():
    return 'hello'


# @home.before_app_first_request
# def create_db():
#     db.create_all()
#     db.session.commit()

# Create a user to test with
@home.before_app_first_request
def create_user():
    for Model in (Role, User, UserRoles):
        Model.drop_table(fail_silently=True)
        Model.create_table(fail_silently=True)
    user_datastore.create_user(email='test@example.com', password='password')
