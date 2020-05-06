from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://ali:Access@localhost/gedii'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
mail = Mail(app)
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'

def create_app(config_name):
    app.config.from_object(config_options[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app