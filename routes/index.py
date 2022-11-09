from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, create_access_token

principal = Blueprint('principal',__name__)

@principal.route('/principal')
@jwt_required()
def index():
    return jsonify({'Mensaje':'Bienvenido!'})