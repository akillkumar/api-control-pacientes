from models.model import *
from utils.antecedentes_personales.schema_habitos_toxicos import *
from flask import  jsonify, request, Blueprint

habitos_toxicos_blueprint = Blueprint('habitos_toxicos',__name__)

@habitos_toxicos_blueprint.route('/habitos_toxicos',methods=['POST'])
def crear_habitos_toxicos():
    try:
        alcohol = request.json['alcohol']
        tabaco = request.json['tabaco']
        drogas = request.json['drogas']
        infusiones = request.json['infusiones']
        antecedentes_personales_id = request.json['antecedentes_personales_id']

        nuevo_habito = Habitos_Toxicos(alcohol=alcohol,tabaco=tabaco,drogas=drogas,infusiones=infusiones,
        estado=True,antecedentes_personales_id=antecedentes_personales_id)

        db.session.add(nuevo_habito)
        db.session.commit()

        return habitos_toxicos_schema.jsonify(nuevo_habito)
    except Exception as e:
        return jsonify({'Error':e})


@habitos_toxicos_blueprint.route('/habitos_toxicos',methods=['GET'])
def obtener_habitos_toxicos():
    habitos_toxicos = Habitos_Toxicos.query.filter_by(estado=True)
    resultados = habitos_toxicos_schemas.dump(habitos_toxicos)

    return jsonify(resultados)

@habitos_toxicos_blueprint.route('/habitos_toxicos/<int:id>',methods=['GET'])
def obtener_habito_toxico(id):
    habito_toxico = Habitos_Toxicos.query.get_or_404(id)
    if habito_toxico.estado != False:
        return habitos_toxicos_schema.jsonify(habito_toxico)
    else:
        return '<h1>no existe el habito toxico </h1>'

@habitos_toxicos_blueprint.route('/habitos_toxicos/<int:id>',methods=['PUT'])
def actualizar_habito_toxico(id):
    habito_toxico = Habitos_Toxicos.query.get_or_404(id)

    alcohol = request.json['alcohol']
    tabaco = request.json['tabaco']
    drogas = request.json['drogas']
    infusiones = request.json['infusiones']

    habito_toxico.alcohol = alcohol
    habito_toxico.tabaco = tabaco 
    habito_toxico.drogas = drogas
    habito_toxico.infusiones = infusiones

    db.session.commit()

    return habitos_toxicos_schema.jsonify(habito_toxico)


@habitos_toxicos_blueprint.route('/habitos_toxicos/<int:id>',methods=['DELETE'])
def eliminar_habito_toxico(id):
    habito_toxico = Habitos_Toxicos.query.get_or_404(id)

    estado = False

    habito_toxico.estado = estado

    db.session.commit()

    return jsonify({'Mensaje':'Se ha eliminado con exito!'})



