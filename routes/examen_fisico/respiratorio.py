from models.model import *
from utils.examen_fisico.schema_respiratorio import *
from flask import  jsonify, request, Blueprint

respiratorio_blueprint = Blueprint('respiratorio',__name__)

@respiratorio_blueprint.route('/respiratorio',methods=['POST'])
def crear_respiratorio():
    try:
        inspeccion = request.json['inspeccion']
        palpacion = request.json['palpacion']
        percusion = request.json['percusion']
        auscultacion = request.json['auscultacion']
        examen_fisico_id = request.json['examen_fisico_id']

        nuevo_respiratorio = Respiratorio(inspeccion=inspeccion,palpacion=palpacion,percusion=percusion,
        auscultacion=auscultacion,estado=True,examen_fisico_id=examen_fisico_id)

        db.session.add(nuevo_respiratorio)
        db.session.commit()
        
        return respiratorio_schema.jsonify(nuevo_respiratorio)
    except Exception as e:

        return jsonify({'Error':e})

@respiratorio_blueprint.route('/respiratorio',methods=['GET'])
def obtener_respiratorios():
    respiratorio = Respiratorio.query.filter_by(estado=True)
    resultado = respiratorio_schemas.dump(respiratorio)
    return jsonify(resultado)

@respiratorio_blueprint.route('/respiratorio/<int:id>', methods=['GET'])
def obtener_respiratorio(id):
    respiratorio = Respiratorio.query.get_or_404(int(id))
    if(respiratorio.estado != False):
        return respiratorio_schema.jsonify(respiratorio)
    else:
        return "<h1>No existe el examen de respiratorio.</h1>"

@respiratorio_blueprint.route('/respiratorio/<int:id>', methods=['PUT'])
def actualizar_respiratorio(id):
    respiratorio = Respiratorio.query.get_or_404(int(id))

    inspeccion = request.json['inspeccion']
    palpacion = request.json['palpacion']
    percusion = request.json['percusion']
    auscultacion = request.json['auscultacion']

    respiratorio.inspeccion=inspeccion
    respiratorio.palpacion=palpacion
    respiratorio.percusion=percusion
    respiratorio.auscultacion=auscultacion

    db.session.commit()

    return respiratorio_schema.jsonify(respiratorio)


@respiratorio_blueprint.route('/respiratorio/<int:id>', methods=['DELETE'])
def eliminar_respiratorio(id):
    respiratorio = Respiratorio.query.get_or_404(int(id))

    estado = False
    respiratorio.estado = estado 
    db.session.commit()

    return respiratorio_schema.jsonify(respiratorio)