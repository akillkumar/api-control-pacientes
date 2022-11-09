from models.model import *
from utils.schema_medicos import *
from flask import  jsonify, request, Blueprint


medicos_blueprint = Blueprint("medicos",__name__)

@medicos_blueprint.route('/medicos', methods=['POST'])
def crear_medico():
    try:
        identificacion = request.json['identificacion']
        primer_nombre = request.json['primer_nombre']
        segundo_nombre = request.json['segundo_nombre']
        primer_apellido= request.json['primer_apellido']
        segundo_apellido= request.json['segundo_apellido']
        especializacion = request.json['especializacion']

        nuevo_medico =  Medicos(identificacion=identificacion,primer_nombre=primer_nombre,segundo_nombre=segundo_nombre,
        primer_apellido=primer_apellido,segundo_apellido=segundo_apellido,especializacion=especializacion,estado=True)

        db.session.add(nuevo_medico)
        db.session.commit()

        return medico_shema.jsonify(nuevo_medico)
    except Exception as e:

        return jsonify({'Error':e})


@medicos_blueprint.route('/medicos',methods=['GET'])
def obtener_medicos():
    medicos = Medicos.query.filter_by(estado=True)

    resultado = medicos_shemas.dump(medicos)

    return jsonify(resultado)


@medicos_blueprint.route('/medicos/<int:id>',methods=['GET'])
def obtener_medico(id):
    medico = Medicos.query.get_or_404(int(id))
    if(medico.estado == False):
        return "<h1>No existe el medico.</h1>"
    else:
        return medico_shema.jsonify(medico)


@medicos_blueprint.route('/medicos/<int:id>',methods=['PUT'])
def actualizar_medico(id):
    medico = Medicos.query.get_or_404(int(id))

    identificacion = request.json['identificacion']
    primer_nombre = request.json['primer_nombre']
    segundo_nombre = request.json['segundo_nombre']
    primer_apellido= request.json['primer_apellido']
    segundo_apellido= request.json['segundo_apellido']
    especializacion = request.json['especializacion']

    medico.identificacion = identificacion
    medico.primer_nombre = primer_nombre
    medico.segundo_nombre = segundo_nombre
    medico.primer_apellido = primer_apellido
    medico.segundo_apellido = segundo_apellido
    medico.especializacion = especializacion

    db.session.commit()

    return medico_shema.jsonify(medico)

@medicos_blueprint.route('/medicos/<int:id>',methods=['DELETE'])
def elimiar_medico(id):
    medico = Medicos.query.get_or_404(int(id))
    estado = False
    medico.estado = estado 
    db.session.commit()

    return medico_shema.jsonify(medico)
