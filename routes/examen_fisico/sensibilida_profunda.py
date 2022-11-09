from models.model import *
from utils.examen_fisico.schema_sensibilidad_profunda import *
from flask import  jsonify, request, Blueprint


sensibilidad_profunda_blueprint = Blueprint('sensibilidad_profunda',__name__)


@sensibilidad_profunda_blueprint.route('/sensibilidad_profunda',methods=['POST'])
def crear_sensibilidad_profunda():
    try:
        dolor_profunda = request.json['dolor_profunda']
        vibratoria = request.json['vibratoria']
        neurologico_id = request.json['neurologico_id']

        nuevo_sensibilidad_profunda = Sensibilidad_Profunda(dolor_profunda=dolor_profunda,vibratoria=vibratoria,estado=True,
        neurologico_id=neurologico_id)

        db.session.add(nuevo_sensibilidad_profunda)
        db.session.commit()
        return sensibilidad_profunda_schema.jsonify(nuevo_sensibilidad_profunda)
    except Exception as e:

        return jsonify({'Error':e})

@sensibilidad_profunda_blueprint.route('/sensibilidad_profunda',methods=['GET'])
def obtener_sensibilidades_profunda():
    sensibilidad_profunda = Sensibilidad_Profunda.query.filter_by(estado=True)
    resultado = sensibilidad_profunda_schemas.dump(sensibilidad_profunda)
    return jsonify(resultado)

@sensibilidad_profunda_blueprint.route('/sensibilidad_profunda/<int:id>',methods=['GET'])
def obtener_sensibilidad_profunda(id):
    sensibilidad_profunda = Sensibilidad_Profunda.query.get_or_404(int(id))
    if sensibilidad_profunda.estado != False:
        
        return sensibilidad_profunda_schema.jsonify(sensibilidad_profunda)
    else:
        return '<h1> no existe sensibilidad profunda </h1>'


@sensibilidad_profunda_blueprint.route('/sensibilidad_profunda/<int:id>',methods=['PUT'])
def actualizar_sensibilidad_profunda(id):
    sensibilidad_profunda = Sensibilidad_Profunda.query.get_or_404(id)

    dolor_profunda = request.json['dolor_profunda']
    vibratoria = request.json['vibratoria']

    sensibilidad_profunda.dolor_profunda = dolor_profunda
    sensibilidad_profunda.vibratoria = vibratoria

    db.session.commit()

    return sensibilidad_profunda_schema.jsonify(sensibilidad_profunda)

@sensibilidad_profunda_blueprint.route('/sensibilidad_profunda/<int:id>', methods=['DELETE'])
def eliminar_sensibilidad_profunda(id):
    sensibilidad_profunda = Sensibilidad_Profunda.query.get_or_404(id)

    estado = False

    sensibilidad_profunda.estado = estado
    db.session.commit()

    return sensibilidad_profunda_schema.jsonify(sensibilidad_profunda)



    
