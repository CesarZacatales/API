from flask import Flask 
from app.routes.user_routes import user_blueprint
from app.routes.robot_routes import robot_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(robot_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
