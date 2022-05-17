import os




class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blogs'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    Class representing the configuration
    '''
DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}    


