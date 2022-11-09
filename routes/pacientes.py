from models.model import *
from utils.schema_pacientes import *
from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

pacientes_blueprint = Blueprint('pacientes',__name__)



@pacientes_blueprint.route('/pacientes',methods=['POST'])
@jwt_required()
def crear_paciente():

    try:
        identificacion = request.json['identificacion']
        primer_nombre = request.json['primer_nombre']
        segundo_nombre = request.json['segundo_nombre']
        primer_apellido= request.json['primer_apellido']
        segundo_apellido= request.json['segundo_apellido']
        genero = request.json['genero']
        fecha_nacimiento = request.json['fecha_nacimiento']
        telefono = request.json['telefono']
        correo= request.json['correo']
        ocupacion = request.json['ocupacion']
        medico_id= request.json['medico_id']

        nuevo_paciente = Pacientes(identificacion=identificacion,primer_nombre=primer_nombre,segundo_nombre=segundo_nombre,
        primer_appellido=primer_apellido,segundo_apellido=segundo_apellido,genero=genero,fecha_nacimiento=fecha_nacimiento,
        telefono=telefono,correo=correo,ocupacion=ocupacion,estado=True,medico_id=medico_id)

        db.session.add(nuevo_paciente)
        db.session.commit()

        return paciente_schema.jsonify(nuevo_paciente)
    except Exception as e:
        return jsonify({'Error':e})


@pacientes_blueprint.route('/pacientes',methods=['GET'])
@jwt_required()
def obtener_pacientes():
    pacientes = Pacientes.query.filter_by(estado=True)

    resutltado = pacientes_schema.dump(pacientes)
    return jsonify(resutltado)

@pacientes_blueprint.route('/pacientes/<id>',methods=['GET'])
@jwt_required()
def obtener_paciente(id):
    paciente = Pacientes.query.get_or_404(int(id))

    if paciente.estado == "false":
        return '<h1>No existe el paciente.</h1>'
    else:
        return paciente_schema.jsonify(paciente)

@pacientes_blueprint.route('/pacientes/<id>', methods=['PUT'])
@jwt_required()
def editar_paciente(id):
    paciente = Pacientes.query.get_or_404(int(id))

    identificacion = request.json['identificacion']
    primer_nombre = request.json['primer_nombre']
    segundo_nombre = request.json['segundo_nombre']
    primer_apellido= request.json['primer_apellido']
    segundo_apellido= request.json['segundo_apellido']
    genero = request.json['genero']
    fecha_nacimiento = request.json['fecha_nacimiento']
    telefono = request.json['telefono']
    correo= request.json['correo']
    ocupacion = request.json['ocupacion']

    paciente.identificacion = identificacion
    paciente.primer_nombre = primer_nombre
    paciente.segundo_nombre = segundo_nombre
    paciente.primer_apellido = primer_apellido
    paciente.segundo_apellido = segundo_apellido
    paciente.genero = genero
    paciente.fecha_nacimiento = fecha_nacimiento
    paciente.telefono = telefono
    paciente.correo = correo
    paciente.ocupacion = ocupacion

    db.session.commit()

    return paciente_schema.jsonify(paciente)

@pacientes_blueprint.route("/pacientes/<id>",methods=['DELETE'])
@jwt_required()
def eliminar_paciente(id):
    paciente = Pacientes.query.get_or_404(int(id))
    estado = False
    paciente.estado = estado

    db.session.commit()

    return paciente_schema.jsonify(paciente)
    