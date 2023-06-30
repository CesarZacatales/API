import os

class Config: 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@mariadb/pdm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


