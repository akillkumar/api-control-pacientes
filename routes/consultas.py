from models.model import *
from utils.schema_consultas import *
from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

consultas_blueprint = Blueprint("motivo-consultas",__name__)

@consultas_blueprint.route('/motivo-consultas',methods=['POST'])
@jwt_required()
def crear_consultas():
    try:
        motivo_consulta = request.json['motivo_consulta']
        enfermedad_actual = request.json['enfermedad_actual']
        antecendentes_enfermedad_ac = request.json['antecedentes_enfermedad_ac']
        antecedentes_familiares = request.json['antecedentes_familiares']
        fecha_consulta = request.json['fecha_consulta']
        paciente_id = request.json['paciente_id']


        nueva_consulta =Consultas(motivo_consulta=motivo_consulta,enfermedad_actual=enfermedad_actual,antecedentes_enfermedad_ac=antecendentes_enfermedad_ac,
        antecedentes_familiares=antecedentes_familiares,fecha_consulta=fecha_consulta,estado=True,paciente_id=paciente_id)

        db.session.add(nueva_consulta)
        db.session.commit()

        return consulta_Schema.jsonify(nueva_consulta)
    except Exception as e:
        return jsonify({'Error':e})

@consultas_blueprint.route('/motivo-consultas',methods=['GET'])
@jwt_required()
def obtener_consultas():
    consultas = Consultas.query.filter_by(estado=True)

    resultado = consultas_Schema.dump(consultas)

    return jsonify(resultado)

@consultas_blueprint.route('/motivo-consultas/<int:id>',methods=['GET'])
@jwt_required()
def obtener_consulta(id):
    consulta = Consultas.query.get_or_404(int(id))
    if(consulta.estado == False):
        return "<h1>No existe la consulta.</h1>"
    else:
        return consulta_Schema.jsonify(consulta)

@consultas_blueprint.route('/motivo-consultas/<int:id>',methods=['PUT'])
def actualizar_consulta(id):
    medico = Medicos.query.get_or_404(int(id))

    motivo_consulta = request.json['motivo_consulta']
    enfermedad_actual = request.json['enfermedad_actual']
    antecendentes_enfermedad_ac = request.json['antecedentes_enfermedad_ac']
    antecedentes_familiares = request.json['antecedentes_familiares']
    fecha_consulta = request.json['fecha_consulta']
    paciente_id = request.json['paciente_id']

    medico.motivo_consulta=motivo_consulta
    medico.enfermedad_actual=enfermedad_actual
    medico.antecedentes_enfermedad_ac=antecendentes_enfermedad_ac
    medico.antecedente_familiares=antecedentes_familiares
    medico.fecha_consulta=fecha_consulta
    paciente_id = paciente_id

    db.session.commit()

    return consulta_Schema.jsonify(medico)


@consultas_blueprint.route('/motivo-consultas/<int:id>',methods=['DELETE'])
@jwt_required()
def elimiar_consulta(id):
    consulta = Consultas.query.get_or_404(int(id))
    estado = False
    consulta.estado = estado 
    db.session.commit()

    return consulta_Schema.jsonify(consulta)