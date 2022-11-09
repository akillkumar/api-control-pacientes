from models.model import *
from utils.examen_fisico.schema_cuello import *
from flask import  jsonify, request, Blueprint

cuello_blueprint = Blueprint('cuello',__name__)

@cuello_blueprint.route('/cuello',methods=['POST'])
def crear_cuello():
    try:
        inspeccion = request.json['inspeccion']
        palpacion = request.json['palpacion']
        percusion = request.json['percusion']
        auscultacion = request.json['auscultacion']
        examen_fisico_id = request.json['examen_fisico_id']

        nuevo_cuello = Cuello(inspeccion=inspeccion,palpacion=palpacion,percusion=percusion,
        auscultacion=auscultacion,estado=True,examen_fisico_id=examen_fisico_id)

        db.session.add(nuevo_cuello)
        db.session.commit()
        
        return cuello_schema.jsonify(nuevo_cuello)
    except Exception as e:

        return jsonify({'Error':e})

@cuello_blueprint.route('/cuello',methods=['GET'])
def obtener_cuellos():
    cuello = Cuello.query.filter_by(estado=True)
    resultado = cuello_schemas.dump(cuello)
    return jsonify(resultado)

@cuello_blueprint.route('/cuello/<int:id>', methods=['GET'])
def obtener_cuello(id):
    cuello = Cuello.query.get_or_404(int(id))
    if(cuello.estado != False):
        return cuello_schema.jsonify(cuello)
    else:
        return "<h1>No existe el examen de cuello.</h1>"

@cuello_blueprint.route('/cuello/<int:id>', methods=['PUT'])
def actualizar_cuello(id):
    cuello = Cuello.query.get_or_404(int(id))

    inspeccion = request.json['inspeccion']
    palpacion = request.json['palpacion']
    percusion = request.json['percusion']
    auscultacion = request.json['auscultacion']

    cuello.inspeccion=inspeccion
    cuello.palpacion=palpacion
    cuello.percusion=percusion
    cuello.auscultacion=auscultacion

    db.session.commit()

    return cuello_schema.jsonify(cuello)


@cuello_blueprint.route('/cuello/<int:id>', methods=['DELETE'])
def eliminar_cuello(id):
    cuello = Cuello.query.get_or_404(int(id))

    estado = False
    cuello.estado = estado 
    db.session.commit()

    return cuello_schema.jsonify(cuello)