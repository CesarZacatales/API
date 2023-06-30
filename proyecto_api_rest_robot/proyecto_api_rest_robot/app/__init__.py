from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from app.routes import user_routes, robot_routes
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(robot_routes.bp)

    return app
