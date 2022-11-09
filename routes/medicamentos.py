from models.model import *
from utils.schema_medicamentos import *
from flask import  jsonify, request, Blueprint


medicamentos_blueprint = Blueprint('medicamentos',__name__)

@medicamentos_blueprint.route('/medicamentos',methods=['POST'])
def crear_medicamentos():
    try:
        nombre = request.json['nombre']
        cantidad = request.json['cantidad']
        formula_medica_id = request.json['formula_medica_id']

        nuevo_medicamento = Medicamentos(nombre=nombre,cantidad=cantidad,estado=True,formula_medica_id=formula_medica_id)

        db.session.add(nuevo_medicamento)
        db.session.commit()

        return medicamentos_schema.jsonify(nuevo_medicamento)
    except Exception as e:
        return jsonify({'Mensaje':e})
@medicamentos_blueprint.route('/medicamentos',methods=['GET'])
def obtener_medicamentos():
    medicamentos = Medicamentos.query.filter_by(estado=True)
    resultados = medicamentos_schemas.dump(medicamentos)

    return jsonify(resultados)
@medicamentos_blueprint.route('/medicamentos/<int:id>',methods=['GET'])
def obtener_medicamento(id):
    medicamento = Medicamentos.query.get_or_404(int(id))
    if medicamento.estado != False:
        return medicamentos_schema.jsonify(medicamento)
    else:
        return '<h1> no existe el medicamento </h1>'

@medicamentos_blueprint.route('/medicamentos/<int:id>',methods=['PUT'])
def actualizar_medicamento(id):
    medicamento = Medicamentos.query.get_or_404(int(id))
    nombre = request.json['nombre']
    cantidad = request.json['cantidad']

    medicamento.nombre = nombre
    medicamento.cantidad = cantidad

    db.session.commit()
    return medicamentos_schema.jsonify(medicamento)

@medicamentos_blueprint.route('/medicamentos/<int:id>',methods=['DELETE'])
def eliminar_medicamento(id):
    medicamento = Medicamentos.query.get_or_404(int(id))

    estado = False
    medicamento.estado = estado

    db.session.commit()

    return jsonify({'Mensaje','se ha eliminado con exito!'})