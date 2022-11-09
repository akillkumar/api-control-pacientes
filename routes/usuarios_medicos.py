
from models.model import *
from utils.schema_usuarios_medicos import *
from utils.schema_medicos import *
from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, create_access_token

usuarios_medicos_blueprint = Blueprint('usuarios_medicos',__name__)


@usuarios_medicos_blueprint.route('/usuarios_medicos', methods=['POST'])
@jwt_required()
def crear_usuarios_medicos():
    try:
        identifacion = request.json['identificacion']
        password = request.json['password']
        medico_id = request.json['medico_id']

        nuevo_usuario = UsuariosMedicos(identificacion=identifacion,password=password,tipo_usuario="Medico",estado=True,medico_id=medico_id)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuarios_medicos_schema.jsonify(nuevo_usuario)
    except Exception as e:
        return jsonify({"Error": e})

@usuarios_medicos_blueprint.route('/usuarios_medicos', methods=['GET'])
@jwt_required()
def obtener_medicos():
    usuarios = UsuariosMedicos.query.filter_by(tipo_usuario="Medico")
    resultados = usuarios_medicos_schemas.dump(usuarios)
   
    return jsonify(resultados)

@usuarios_medicos_blueprint.route('/usuarios_medicos/<int:id>', methods=['GET'])
@jwt_required()
def obtener_medico(id):
    usuario = UsuariosMedicos.query.get_or_404(int(id))
   
    if usuario.estado != False:
        usuarioMedico(id)
    
        return usuarios_medicos_schema.jsonify(usuario)
    else:
        return '<h1>no se encuentra este usuario medico </h1>'

@usuarios_medicos_blueprint.route('/usuarios_medicos/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_medico(id):
    usuario = UsuariosMedicos.query.get_or_404(int(id))
    identifacion = request.json['identificacion']
    password = request.json['password']

    usuario.identificacion = identifacion
    usuario.password = password

    db.session.commit()
    return usuarios_medicos_schema.jsonify(usuario)
    
    
@usuarios_medicos_blueprint.route('/usuarios_medicos/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_medico(id):
    usuario = UsuariosMedicos.query.get_or_404(int(id))
    estado = False

    usuario.estado = estado
    db.session.commit()
    return jsonify({"Mensaje":"se ha eliminado con exito!"})


@usuarios_medicos_blueprint.route('/usuarios_medicos/login', methods=['POST'])
def login():
    if request.is_json:
        identificacion = request.json['identificacion']
        password = request.json['password']
    else:
        identificacion = request.form['identificacion']
        password = request.form['password']

    test = UsuariosMedicos.query.filter_by(identificacion=identificacion, password=password).first()
    
    
    if test:
        access_token = create_access_token(identity=identificacion)
       
        return jsonify(message='Login Successful', access_token=access_token,success=True)
    else:
        return jsonify({"message":"Identificacion o Contraseña incorrectos!",
        "success":False})

def usuarioMedico(id):
    medico = Medicos.query.join(UsuariosMedicos).filter_by(id=id).first()
    resul = JoinUsuariosMedicosConMedico_schemas.jsonify(medico)
    print(resul)
    return JoinUsuariosMedicosConMedico_schemas.jsonify(medico)


