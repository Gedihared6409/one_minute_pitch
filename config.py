import os
class Config:

    SECRET_KEY = 'Access'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ali:Access@localhost/gedii'

    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'gediali@gmail.com'
class ProdConfig(Config):

    pass
class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ali:Access@localhost/gedii'
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}

