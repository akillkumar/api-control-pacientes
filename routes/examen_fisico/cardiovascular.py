from models.model import *
from utils.examen_fisico.schema_cardiovascular import *
from flask import  jsonify, request, Blueprint

cardiovascular_blueprint = Blueprint('cardiovascular',__name__)

@cardiovascular_blueprint.route('/cardiovascular',methods=['POST'])
def crear_cardiovascular():
    try:
        inspeccion = request.json['inspeccion']
        palpacion = request.json['palpacion']
        auscultacion = request.json['auscultacion']
        pulsos = request.json['pulsos']
        examen_fisico_id = request.json['examen_fisico_id']

        nuevo_cardiovascular = Cardiovascular(inspeccion=inspeccion,palpacion=palpacion,auscultacion=auscultacion,
        pulsos=pulsos,estado=True,examen_fisico_id=examen_fisico_id)

        db.session.add(nuevo_cardiovascular)
        db.session.commit()
        
        return cardiovascular_schema.jsonify(nuevo_cardiovascular)
    except Exception as e:

        return jsonify({'Error':e})

@cardiovascular_blueprint.route('/cardiovascular',methods=['GET'])
def obtener_cardiovasculars():
    cardiovascular = Cardiovascular.query.filter_by(estado=True)
    resultado = cardiovascular_schemas.dump(cardiovascular)
    return jsonify(resultado)

@cardiovascular_blueprint.route('/cardiovascular/<int:id>', methods=['GET'])
def obtener_cardiovascular(id):
    cardiovascular = Cardiovascular.query.get_or_404(int(id))
    if(cardiovascular.estado != False):
        return cardiovascular_schema.jsonify(cardiovascular)
    else:
        return "<h1>No existe el examen de cardiovascular.</h1>"

@cardiovascular_blueprint.route('/cardiovascular/<int:id>', methods=['PUT'])
def actualizar_cardiovascular(id):
    cardiovascular = Cardiovascular.query.get_or_404(int(id))

    inspeccion = request.json['inspeccion']
    palpacion = request.json['palpacion']
    auscultacion = request.json['auscultacion']
    pulsos = request.json['pulsos']

    cardiovascular.inspeccion=inspeccion
    cardiovascular.palpacion=palpacion
    cardiovascular.auscultacion=auscultacion
    cardiovascular.pulsos=pulsos

    db.session.commit()

    return cardiovascular_schema.jsonify(cardiovascular)


@cardiovascular_blueprint.route('/cardiovascular/<int:id>', methods=['DELETE'])
def eliminar_cardiovascular(id):
    cardiovascular = Cardiovascular.query.get_or_404(int(id))

    estado = False
    cardiovascular.estado = estado 
    db.session.commit()

    return cardiovascular_schema.jsonify(cardiovascular)