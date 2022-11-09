from models.model import *
from utils.antecedentes_personales.schema_antecedentes_personales import *
from flask import  jsonify, request, Blueprint


antecedentes_personales_blueprint = Blueprint('antecedentes_personales',__name__)

@antecedentes_personales_blueprint.route('/antecedentes_personales',methods=['POST'])
def crear_antecedente():
    try:
        enfermedad_de_infancia = request.json['enfermedad_de_infancia']
        consulta_id = request.json['consulta_id']
        nuevo_antecedente = Antecedentes_Personales(enfermedad_de_infancia=enfermedad_de_infancia,estado=True,
        consulta_id=consulta_id)

        db.session.add(nuevo_antecedente)
        db.session.commit()

        return antecedentes_personales_schema.jsonify(nuevo_antecedente)
    except Exception as e:
        return jsonify({'MEnsaje':e})

@antecedentes_personales_blueprint.route('/antecedentes_personales',methods=['GET'])
def obtener_antecedentes():
    antecedentes = Antecedentes_Personales.query.filter_by(estado=True)

    resultados = antecedentes_personales_schemas.dump(antecedentes)

    return jsonify(resultados)

@antecedentes_personales_blueprint.route('/antecedentes_personales/<int:id>',methods=['GET'])
def obtener_antecedente(id):
    antecedente = Antecedentes_Personales.query.get_or_404(int(id))
    if antecedente.estado != False:
        return antecedentes_personales_schema.jsonify(antecedente)
    else:
        return '<h1> no se encuentra el antecedente personal </h1>'

@antecedentes_personales_blueprint.route('/antecedentes_personales/<int:id>',methods=['PUT'])
def actualizar_antecedente(id):
    antecedente = Antecedentes_Personales.query.get_or_404(int(id))

    enfermedad_de_infancia = request.json['enfermedad_de_infancia']
    antecedente.enfermedad_de_infancia = enfermedad_de_infancia

    db.session.commit()

    return antecedentes_personales_schema.jsonify(antecedente)


@antecedentes_personales_blueprint.route('/antecedentes_personales/<int:id>',methods=['DELETE'])
def eliminar_antecedente(id):
    antecedente = Antecedentes_Personales.query.get_or_404(int(id))

    estado = False
    antecedente.estado = estado

    db.session.commit()

    return jsonify({'Mensaje':'Ha sido eliminado con exito!'})