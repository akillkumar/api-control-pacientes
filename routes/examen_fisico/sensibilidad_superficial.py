from re import T
from models.model import *
from utils.examen_fisico.schema_sensibilidad_superficial import *
from flask import  jsonify, request, Blueprint

sensibilidad_superficial_blueprint = Blueprint('sensibilidad_superficial',__name__)

@sensibilidad_superficial_blueprint.route('/sensibilidad_superficial',methods=['POST'])
def crear_sensibilidad_superficial():
    try:
        tactil = request.json['tactil']
        dolorosa = request.json['dolorosa']
        termica = request.json['termica']
        neurologico_id = request.json['neurologico_id']

        nuevo_sensibilidad_superficial = Sensibilidad_Superficial(tactil=tactil,dolorosa=dolorosa,termica=termica,
        estado=True,neurologico_id=neurologico_id)

        db.session.add(nuevo_sensibilidad_superficial)
        db.session.commit()

        return sensibilidad_superficial_schema.jsonify(nuevo_sensibilidad_superficial)
    except Exception as e:
        return jsonify({"Error": e})

@sensibilidad_superficial_blueprint.route('/sensibilidad_superficial',methods=['GET'])
def obtener_sensibilidades_superficiales():
    sensibilidad_superficial = Sensibilidad_Superficial.query.filter_by(estado = True)
    resultado = sensibilidad_superficial_schemas.dump(sensibilidad_superficial)
    return jsonify(resultado)

@sensibilidad_superficial_blueprint.route('/sensibilidad_superficial/<int:id>', methods=['GET'])
def obtener_sensibilidad_superficial(id):
    sensibilidad_superficial = Sensibilidad_Superficial.query.get_or_404(id)
    if sensibilidad_superficial.estado != False:
        return sensibilidad_superficial_schema.jsonify(sensibilidad_superficial)
    else:
        return '<h1>no se encontro la sensibilidad superficial </h1>'

@sensibilidad_superficial_blueprint.route('/sensibilidad_superficial/<int:id>',methods=['PUT'])
def actualizar_sensibilidad_superficial(id):
    sensibilidad_superficial = Sensibilidad_Superficial.query.get_or_404(id)

    tactil = request.json['tactil']
    dolorosa = request.json['dolorosa']
    termica = request.json['termica']

    sensibilidad_superficial.tactil = tactil
    sensibilidad_superficial.dolorosa = dolorosa
    sensibilidad_superficial.termica = termica

    db.session.commit()

    return sensibilidad_superficial_schema.jsonify(sensibilidad_superficial)


@sensibilidad_superficial_blueprint.route('/sensibilidad_superficial/<int:id>',methods=['DELETE'])
def eliminar_sensibilidad_superficial(id):
    sensibilidad_superficial = Sensibilidad_Superficial.query.get_or_404(id)

    estado = False

    sensibilidad_superficial.estado = estado

    return jsonify({"Mensaje":"Se ha eliminado con exito!"})
