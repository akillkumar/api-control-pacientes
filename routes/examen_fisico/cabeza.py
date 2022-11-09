from models.model import *
from utils.examen_fisico.schema_cabeza import *
from flask import  jsonify, request, Blueprint

cabeza_blueprint = Blueprint('cabeza',__name__)

@cabeza_blueprint.route('/cabeza',methods=['POST'])
def crear_cabeza():
    try:
        craneo_y_cara = request.json['craneo_y_cara']
        cuero_cabelludo = request.json['cuero_cabelludo']
        region_frontal = request.json['region_frontal']
        region_obitonasal = request.json['region_obitonasal']
        region_orinfarengea = request.json['region_orinfarengea']
        examen_fisico_id = request.json['examen_fisico_id']

        nueva_cabeza = Cabeza(craneo_y_cara=craneo_y_cara,cuero_cabelludo=cuero_cabelludo,region_frontal=region_frontal,
        region_obitonasal=region_obitonasal,region_orinfarengea=region_orinfarengea,estado=True,examen_fisico_id=examen_fisico_id)

        db.session.add(nueva_cabeza)
        db.session.commit()

        return cabeza_schema.jsonify(nueva_cabeza)
    except Exception as e:
        return jsonify({"error":e})


@cabeza_blueprint.route('/cabeza',methods=['GET'])
def obtener_cabezas():
    cabeza = Cabeza.query.filter_by(estado=True)
    resultado = cabeza_schemas.dump(cabeza)
    return jsonify(resultado)

@cabeza_blueprint.route('/cabeza/<int:id>',methods=['GET'])
def obtener_cabeza(id):
    cabeza = Cabeza.query.get_or_404(int(id))
    if cabeza.estado != False:
        return cabeza_schema.jsonify(cabeza)
    else:
        return '<h1>no existe el examen de cabeza </h1>'

@cabeza_blueprint.route('/cabeza/<int:id>',methods=['PUT'])
def actualizar_cabeza(id):
    cabeza = Cabeza.query.get_or_404(int(id))

    craneo_y_cara = request.json['craneo_y_cara']
    cuero_cabelludo = request.json['cuero_cabelludo']
    region_frontal = request.json['region_frontal']
    region_obitonasal = request.json['region_obitonasal']
    region_orinfarengea = request.json['region_orinfarengea']

    cabeza.craneo_y_cara = craneo_y_cara
    cabeza.cuero_cabelludo = cuero_cabelludo
    cabeza.region_frontal = region_frontal
    cabeza.region_obitonasal = region_obitonasal
    cabeza.region_orinfarengea = region_orinfarengea

    db.session.commit()

    return cabeza_schema.jsonify(cabeza)

@cabeza_blueprint.route('/cabeza/<int:id>',methods=['DELETE'])
def eliminar_cabeza(id):
    cabeza = Cabeza.query.get_or_404(int(id))

    estado = False
    cabeza.estado = estado
    return jsonify({"mensaje":"se ha eliminado con exito"})
