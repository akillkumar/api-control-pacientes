from models.model import *
from utils.schema_citas_asignadas import *
from flask import  jsonify, request, Blueprint

citas_asignadas_blueprint = Blueprint('citas_asignadas',__name__)

@citas_asignadas_blueprint.route('/citas_asignadas',methods=['POST'])
def crear_citas_asignadas():
    try:
        fecha = request.json['fecha']
        hora = request.json['hora']
        paciente_id = request.json['paciente_id']
        solicitud_cita_paciente_id = request.json['solicitud_cita_paciente_id']

        nuevo_cita = Citas_Asignadas(fecha=fecha,hora=hora,estado=True,paciente_id=paciente_id,solicitud_cita_paciente_id=solicitud_cita_paciente_id)

        db.session.add(nuevo_cita)
        db.session.commit()

        return citas_asignadas_schema.jsonify(nuevo_cita)
    except Exception as e:
        return jsonify({"error":e})

@citas_asignadas_blueprint.route('/citas_asignadas',methods=['GET'])
def obtener_citas_asignadas():
    citas_asignadas = Citas_Asignadas.query.filter_by(estado=True)
    resultado = citas_asignadas_schemas.dump(citas_asignadas)

    return jsonify(resultado)
@citas_asignadas_blueprint.route('/citas_asignadas/<int:id>',methods=['GET'])
def obtener_cita_asignada(id):
    cita_asignada = Citas_Asignadas.query.get_or_404(int(id))
    if cita_asignada.estado != null:
        return citas_asignadas_schema.jsonify(cita_asignada)
    else:
        return '<h1> no existe la cita asignada </h1>'
@citas_asignadas_blueprint.route('/citas_asignadas/<int:id>',methods=['PUT'])
def actualizar_cita_asignada(id):
    cita_asignada = Citas_Asignadas.query.get_or_404(int(id))

    fecha = request.json['fecha']
    hora = request.json['hora']

    cita_asignada.fecha = fecha
    cita_asignada.hora = hora

    db.session.commit()
    return citas_asignadas_schema.jsonify(cita_asignada)

@citas_asignadas_blueprint.route('/citas_asignadas/<int:id>',methods=['DELETE'])
def eliminar_cita_asignada(id):
    cita_asignada = Citas_Asignadas.query.get_or_404(int(id))

    estado = False
    cita_asignada.estado = estado

    db.session.commit()
    return jsonify({"Mensaje":"Se ha eliminado con exito!"})