from quickvue.core.models import User, user_schema

def get_user_info(user_id):
    return user_schema.dump(User.get_by_id(user_id))
