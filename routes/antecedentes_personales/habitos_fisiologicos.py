from models.model import *
from utils.antecedentes_personales.schema_habitos_fisiologicos import *
from flask import  jsonify, request, Blueprint

habitos_fisiologicos_blueprint = Blueprint('habitos_fisiologicos',__name__)


@habitos_fisiologicos_blueprint.route('/habitos_fisiologicos',methods=['POST'])
def crear_habitos_fisiologicos():
    try:
        alimentacion = request.json['alimentacion']
        diuresis = request.json['diuresis']
        catarsis = request.json['catarsis']
        sueño = request.json['sueño']
        sexualidad = request.json['sexualidad']
        otros = request.json['otros']
        antecedentes_personales_id = request.json['antecedentes_personales_id']

        nuevo_habito = Habitos_Fisiologicos(alimentacion=alimentacion,diuresis=diuresis,catarsis=catarsis,sueño=sueño,
        sexualidad=sexualidad,otros=otros,estado=True,antecedentes_personales_id=antecedentes_personales_id)

        db.session.add(nuevo_habito)
        db.session.commit()

        return habitos_fisiologicos_schema.jsonify(nuevo_habito)
    except Exception as e:
        return jsonify({"error":e})


@habitos_fisiologicos_blueprint.route('/habitos_fisiologicos',methods=['GET'])
def obtener_habitos_fisiologicos():
    habitos_fisiologicos = Habitos_Fisiologicos.query.filter_by(estado=True)
    resultados = habitos_fisiologicos_schemas.dump(habitos_fisiologicos)
    return jsonify(resultados)

@habitos_fisiologicos_blueprint.route('/habitos_fisiologicos/<int:id>',methods=['GET'])
def obtener_habito_fisiologico(id):
    habito_fisiologico = Habitos_Fisiologicos.query.get_or_404(id)
    if habito_fisiologico.estado != False:
        return habitos_fisiologicos_schema.jsonify(habito_fisiologico)
    else:
        return '<h1> no existe el habito fisiologico </h1>'

@habitos_fisiologicos_blueprint.route('/habitos_fisiologicos/<int:id>',methods=['PUT'])
def actualizar_habito_fisiologico(id):
    habito_fisiologico = Habitos_Fisiologicos.query.get_or_404(id)
    alimentacion = request.json['alimentacion']
    diuresis = request.json['diuresis']
    catarsis = request.json['catarsis']
    sueño = request.json['sueño']
    sexualidad = request.json['sexualidad']
    otros = request.json['otros']

    habito_fisiologico.alimentacion =alimentacion
    habito_fisiologico.diuresis =diuresis
    habito_fisiologico.catarsis =catarsis
    habito_fisiologico.sueño =sueño
    habito_fisiologico.sexualidad =sexualidad
    habito_fisiologico.otros =otros

    db.session.commit()

    return habitos_fisiologicos_schema.jsonify(habito_fisiologico)


@habitos_fisiologicos_blueprint.route('/habitos_fisiologicos/<int:id>',methods=['DELETE'])
def eliminar_habito_fisiologico(id):
    habito_fisiologico = Habitos_Fisiologicos.query.get_or_404(id)

    estado = False

    habito_fisiologico.estado = estado

    db.session.commit()

    return jsonify({"Mensaje":"Se ha eliminado exitosamente!"})




