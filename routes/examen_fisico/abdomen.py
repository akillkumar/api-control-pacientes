from models.model import *
from utils.examen_fisico.schema_abdomen import *
from flask import  jsonify, request, Blueprint

abdomen_blueprint = Blueprint('abdomen',__name__)

@abdomen_blueprint.route('/abdomen',methods=['POST'])
def crear_abdomen():
    try:
        inspeccion = request.json['inspeccion']
        palpacion = request.json['palpacion']
        percusion = request.json['percusion']
        auscultacion = request.json['auscultacion']
        examen_fisico_id = request.json['examen_fisico_id']

        nuevo_abdomen = Abdomen(inspeccion=inspeccion,palpacion=palpacion,percusion=percusion,
        auscultacion=auscultacion,estado=True,examen_fisico_id=examen_fisico_id)

        db.session.add(nuevo_abdomen)
        db.session.commit()
        
        return abdomen_schema.jsonify(nuevo_abdomen)
    except Exception as e:

        return jsonify({'Error':e})

@abdomen_blueprint.route('/abdomen',methods=['GET'])
def obtener_abdomens():
    abdomen = Abdomen.query.filter_by(estado=True)
    resultado = abdomen_schemas.dump(abdomen)
    return jsonify(resultado)

@abdomen_blueprint.route('/abdomen/<int:id>', methods=['GET'])
def obtener_abdomen(id):
    abdomen = Abdomen.query.get_or_404(int(id))
    if(abdomen.estado != False):
        return abdomen_schema.jsonify(abdomen)
    else:
        return "<h1>No existe el examen de abdomen.</h1>"

@abdomen_blueprint.route('/abdomen/<int:id>', methods=['PUT'])
def actualizar_abdomen(id):
    abdomen = Abdomen.query.get_or_404(int(id))

    inspeccion = request.json['inspeccion']
    palpacion = request.json['palpacion']
    percusion = request.json['percusion']
    auscultacion = request.json['auscultacion']

    abdomen.inspeccion=inspeccion
    abdomen.palpacion=palpacion
    abdomen.percusion=percusion
    abdomen.auscultacion=auscultacion

    db.session.commit()

    return abdomen_schema.jsonify(abdomen)


@abdomen_blueprint.route('/abdomen/<int:id>', methods=['DELETE'])
def eliminar_abdomen(id):
    abdomen = Abdomen.query.get_or_404(int(id))

    estado = False
    abdomen.estado = estado 
    db.session.commit()

    return abdomen_schema.jsonify(abdomen)