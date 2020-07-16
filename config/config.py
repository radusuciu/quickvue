"""Main configuration file for project."""

import yaml
import os
import pathlib


PROJECT_NAME = 'quickvue'
PROJECT_HOME_PATH = pathlib.Path(os.path.realpath(__file__)).parents[1]


# debug is true by default
DEBUG = bool(os.getenv('DEBUG', True))
_secrets_path = PROJECT_HOME_PATH.joinpath('config', 'secrets.yml')
_override_path = PROJECT_HOME_PATH.joinpath('config', 'secrets.override.yml')

# get our secrets
with _secrets_path.open() as f:
    _SECRETS = yaml.load(f)

# provide a mechanism for overriding some secrets
if _override_path.is_file():
    with _override_path.open() as f:
        _SECRETS.update(yaml.load(f))

class _Config(object):
    """Holds flask configuration to be consumed by Flask's from_object method."""

    # Peewee
    DATABASE = 'sqlite:////{}/quickvue.db'.format(str(PROJECT_HOME_PATH))

    # Flask
    DEBUG = False
    SECRET_KEY = _SECRETS['flask']['SECRET_KEY']
    JSONIFY_PRETTYPRINT_REGULAR = False

    # Flask-Security
    SECURITY_PASSWORD_SALT = _SECRETS['flask-security']['SECURITY_PASSWORD_SALT']
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False

class _DevelopmentConfig(_Config):
    """Configuration for development environment."""

    DEBUG = True

config = _DevelopmentConfig if DEBUG else _Config
