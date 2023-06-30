from flask import Blueprint, request, jsonify
from app.models.robot import Robot

robot_blueprint = Blueprint('robot_blueprint', __name__)

@robot_blueprint.route('/robot', methods=['POST'])
def create_robot():
    auth = request.authorization
    user = User.query.filter_by(name=auth.username).first()
    if user:
        data = request.get_json()
        new_robot = Robot(name=data['name'], imei=data['imei'], user_id=user.id)
        # aquí va el código para guardar el nuevo robot en la base de datos
        return jsonify({'message': 'Robot registered successfully'})
    return jsonify({'message': 'User not found'}), 404
