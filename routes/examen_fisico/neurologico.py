from models.model import *
from utils.examen_fisico.schema_neurologico import *
from flask import  jsonify, request, Blueprint

neurologico_blueprint = Blueprint('neurologico',__name__)

@neurologico_blueprint.route('/neurologico', methods=['POST'])
def crear_neurologico():
    try:
        glasgow = request.json['glasgow']
        motilidad_activa = request.json['motilidad_activa']
        motilidad_pasiva = request.json['motilidad_pasiva']
        motilidad_refleja = request.json['motilidad_refleja']
        pares_craneales = request.json['pares_craneales']
        examen_fisico_id = request.json['examen_fisico_id']

        nuevo_neurologico = Neurologico(glasgow=glasgow,motilidad_activa=motilidad_activa,motilidad_pasiva=motilidad_pasiva,
        motilidad_refleja=motilidad_refleja,pares_craneales=pares_craneales,estado=True,examen_fisico_id=examen_fisico_id)

        db.session.add(nuevo_neurologico)
        db.session.commit()

        return neurologico_schema.jsonify(nuevo_neurologico)
    except Exception as e:
        return jsonify({"error": e})


@neurologico_blueprint.route('/neurologico',methods=['GET'])
def obtener_neurologicos():
    neurologico = Neurologico.query.filter_by(estado=True)
    resultado = neuorlogico_schemas.dump(neurologico)
    return jsonify(resultado)

@neurologico_blueprint.route('/neurologico/<int:id>',methods=['GET'])
def obtener_neurologico(id):
    neurologico = Neurologico.query.get_or_404(int(id))
    if neurologico.estado != False:
        return neurologico_schema.jsonify(neurologico)
    else:
        return "<h1>No existe el examen neurologico.</h1>"

@neurologico_blueprint.route('/neurologico/<int:id>',methods=['PUT'])
def actualizar_neurologico(id):
    neurologico = Neurologico.query.get_or_404(int(id))

    glasgow = request.json['glasgow']
    motilidad_activa = request.json['motilidad_activa']
    motilidad_pasiva = request.json['motilidad_pasiva']
    motilidad_refleja = request.json['motilidad_refleja']
    pares_craneales = request.json['pares_craneales']

    neurologico.glasgow = glasgow
    neurologico.motilidad_activa = motilidad_activa
    neurologico.motilidad_pasiva = motilidad_pasiva
    neurologico.motilidad_refleja = motilidad_refleja
    neurologico.pares_craneales = pares_craneales

    db.session.commit()

    return neurologico_schema.jsonify(neurologico)

@neurologico_blueprint.route('/neurologico/<int:id>',methods=['DELETE'])
def eliminar_neurologico(id):
    neurologico = Neurologico.query.get_or_404(int(id))

    estado = False
    neurologico.estado = estado
    db.session.commit()

    return jsonify({"Mensaje":"Se ha eliminado con exito!"})