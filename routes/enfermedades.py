from models.model import *
from utils.schema_enfermedades import *
from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
enfermedades_blueprint = Blueprint('enfermedades',__name__)


@enfermedades_blueprint.route('/enfermedades',methods=['POST'])
@jwt_required()
def crear_enfermedad():
    try:
        cv = request.json['cv']
        respiratorio = request.json['respiratorio']
        nefrourologicos = request.json['nefrourologicos']
        neurologicos = request.json['neurologicos']
        hematologicos = request.json['hematologicos']
        infectologicos = request.json['infectologicos']
        endocrinologicos = request.json['endocrinologicos']
        quirurgicos = request.json['quirurgicos']
        traumatologicos = request.json['traumatologicos']
        alergicos = request.json['alergicos']
        epidemiologicos = request.json['epidemiologicos']
        antecedentes_heredofamiliares = request.json['antecedentes_heredofamiliares']
        consulta_id = request.json['consulta_id']

        nueva_enfermedad = Enfermedades(cv=cv,respiratorio=respiratorio,nefrourologicos=nefrourologicos,neurologicos=neurologicos,hematologicos=hematologicos,
        infectologicos=infectologicos,endocrinologicos=endocrinologicos,quirurgicos=quirurgicos,traumatologicos=traumatologicos,alergicos=alergicos,
        epidemiologicos=epidemiologicos,antecedentes_heredofamiliares=antecedentes_heredofamiliares,estado=True,consulta_id=consulta_id)

        db.session.add(nueva_enfermedad)
        db.session.commit()

        return enfermedades_schema.jsonify(nueva_enfermedad)
    except Exception as e:
        return jsonify({"Error": e})
    
@enfermedades_blueprint.route('/enfermedades',methods=['GET'])
@jwt_required()
def obtener_enfermedades():
    enfermedades = Enfermedades.query.filter_by(estado=True)
    resultado = enfermedades_schemas.dump(enfermedades)
    return jsonify(resultado)

@enfermedades_blueprint.route('/enfermedades/<int:id>',methods=['GET'])
@jwt_required()
def obtener_enfermedad(id):
    enfermedad = Enfermedades.query.get_or_404(int(id))
    if enfermedad.estado != False or enfermedad.id == id:
        return enfermedades_schema.jsonify(enfermedad)
    else:
        return '<h1>no existe la enfermedad </h1>'

@enfermedades_blueprint.route('/enfermedades/<int:id>',methods=['PUT'])
@jwt_required()
def actualizar_enfermedad(id):
    enfermedad = Enfermedades.query.get_or_404(int(id))

    cv = request.json['cv']
    respiratorio = request.json['respiratorio']
    nefrourologicos = request.json['nefrourologicos']
    neurologicos = request.json['neurologicos']
    hematologicos = request.json['hematologicos']
    infectologicos = request.json['infectologicos']
    endocrinologicos = request.json['endocrinologicos']
    quirurgicos = request.json['quirurgicos']
    traumatologicos = request.json['traumatologicos']
    alergicos = request.json['alergicos']
    epidemiologicos = request.json['epidemiologicos']
    antecedentes_heredofamiliares = request.json['antecedentes_heredofamiliares']

    enfermedad.cv =cv
    enfermedad.respiratorio =respiratorio
    enfermedad.nefrourologicos =nefrourologicos
    enfermedad.neurologicos = neurologicos
    enfermedad.hematologicos =hematologicos
    enfermedad.infectologicos = infectologicos
    enfermedad.endocrinologicos =endocrinologicos
    enfermedad.quirurgicos =quirurgicos
    enfermedad.traumatologicos =traumatologicos
    enfermedad.alergicos =alergicos
    enfermedad.epidemiologicos =epidemiologicos
    enfermedad.antecedentes_heredofamiliares =antecedentes_heredofamiliares

    db.session.commit()

    return enfermedades_schema.jsonify(enfermedad)



@enfermedades_blueprint.route('/enfermedades/<int:id>',methods=['DELETE'])
@jwt_required()
def eliminar_enfermedad(id):
    enfermedad = Enfermedades.query.get_or_404(int(id))
    estado = False

    enfermedad.estado = estado

    db.session.commit()

    return jsonify({"Mensaje":"Se ha eliminado con exito!"})