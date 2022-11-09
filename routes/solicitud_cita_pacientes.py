from models.model import *
from utils.schema_solicitud_cita_pacientes import *
from flask import  jsonify, request, Blueprint

s_c_p_blueprint = Blueprint('s_c_p',__name__)

@s_c_p_blueprint.route('/s_c_p', methods=['POST'])
def crear_s_c_p():
    try:
        paciente_id = request.json['paciente_id']
        nuevo_s_c_p = Solicitud_Cita_Pacientes(estado=True,paciente_id=paciente_id)
        db.session.add(nuevo_s_c_p)
        db.session.commit()
        return s_c_p_schema.jsonify(nuevo_s_c_p)
    except Exception as e:
        return jsonify({"error":e})
    
@s_c_p_blueprint.route('/s_c_p', methods=['GET'])
def obtener_s_c_p():
    s_c_p = Solicitud_Cita_Pacientes.query.filter_by(estado=True)
    resultado = s_c_p_schemas.dump(s_c_p)
    return jsonify(resultado)
@s_c_p_blueprint.route('/s_c_p/<int:id>', methods=['GET'])
def obtener_s_c_ps(id):
    s_c_p = Solicitud_Cita_Pacientes.query.get_or_404(int(id))
    if s_c_p.estado != False:
        return s_c_p_schema.jsonify(s_c_p)
    else:
        return '<h1> no existe esta solicitud </h1>'
@s_c_p_blueprint.route('/s_c_p/<int:id>', methods=['DELETE'])
def eliminar_solicitud(id):
    s_c_p = Solicitud_Cita_Pacientes.query.get_or_404(int(id))

    db.session.delete(s_c_p)
    db.session.commit()
    return jsonify({"Mensaje":"se ha elimanado con exito!"})