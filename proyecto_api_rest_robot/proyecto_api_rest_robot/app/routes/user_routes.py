from flask import Blueprint, request, jsonify, make_response
from app.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/user/register', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    # aquí va el código para guardar el nuevo usuario en la base de datos
    return make_response(jsonify({'message': 'Registered successfully'}), 201)

@user_blueprint.route('/user/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    user = User.query.filter_by(name=auth.username).first()
    if check_password_hash(user.password, auth.password):
        # aquí va el código para manejar la sesión del usuario
        return jsonify({'message': 'Logged in successfully'})
    return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
