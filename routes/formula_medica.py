from models.model import *
from utils.schema_formula_medica import *
from flask import  jsonify, request, Blueprint

formula_medica_blueprint = Blueprint('formula_medica',__name__)

@formula_medica_blueprint.route('/formula_medica',methods=['POST'])
def crear_formula_medica():
    try:
        preescribe = request.json['preescribe']
        recomendacion = request.json['recomendacion']
        fecha_inicio = request.json['fecha_inicio']
        fecha_fin = request.json['fecha_fin']
        observaciones = request.json['observaciones']
        paciente_id = request.json['paciente_id']

        nueva_formula = Formula_Medica(preescribe=preescribe,recomendacion=recomendacion,fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,observaciones=observaciones,estado=True,paciente_id=paciente_id)

        db.session.add(nueva_formula)
        db.session.commit()

        return formula_medica_schema.jsonify(nueva_formula)
    except Exception as e:
        return jsonify({"Error":e})

@formula_medica_blueprint.route('/formula_medica',methods=['GET'])
def obtener_formulas_medicas():
    formulas_medicas = Formula_Medica.query.filter_by(estado=True)
    resultados = formula_medica_schemas.dump(formulas_medicas)
    return jsonify(resultados)
@formula_medica_blueprint.route('/formula_medica/<int:id>',methods=['GET'])
def obtener_formula_medica(id):
    formulas_medicas = Formula_Medica.query.get_or_404(int(id))
    if formulas_medicas.estado != False:
        return formula_medica_schema.jsonify(formulas_medicas)
    else:
        return '<h1> no existe la formula medica </h1>'
@formula_medica_blueprint.route('/formula_medica/<int:id>',methods=['PUT'])
def actualizar_formula_medica(id):
    formulas_medicas = Formula_Medica.query.get_or_404(int(id))

    preescribe = request.json['preescribe']
    recomendacion = request.json['recomendacion']
    fecha_inicio = request.json['fecha_inicio']
    fecha_fin = request.json['fecha_fin']
    observaciones = request.json['observaciones']

    formulas_medicas.preescribe = preescribe
    formulas_medicas.recomendacion = recomendacion
    formulas_medicas.fecha_inicio = fecha_inicio
    formulas_medicas.fecha_fin = fecha_fin
    formulas_medicas.observaciones = observaciones

    db.session.commit()

    return formula_medica_schema.jsonify(formulas_medicas)

@formula_medica_blueprint.route('/formula_medica/<int:id>',methods=['DELETE'])
def eliminar_formula_medica(id):
    formulas_medicas = Formula_Medica.query.get_or_404(int(id))

    estado = False
    formulas_medicas.estado = estado

    db.session.commit()
    return jsonify({"Mensaje":"Se ha eliminado con exito!"})