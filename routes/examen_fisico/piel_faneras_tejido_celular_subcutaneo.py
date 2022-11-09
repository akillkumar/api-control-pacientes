from models.model import *
from utils.examen_fisico.schema_piel_faneras_tejido_celular_subcutaneo import *
from flask import  jsonify, request, Blueprint

pftcs_blueprint = Blueprint('pftcs',__name__)

@pftcs_blueprint.route('/pftcs',methods=['POST'])
def crear_pftcs():
    try:
        aspecto= request.json['aspecto']
        distribucion_pilosa= request.json['distribucion_pilosa']
        lesiones= request.json['lesiones']
        faneras= request.json['faneras']
        t_c_subcutaneo= request.json['t_c_subcutaneo']
        examen_fisico_id= request.json['examen_fisico_id']

        nuevo_pftcs = Piel_Faneras_Tejido_Celular_Subcutaneo(aspecto=aspecto,distribucion_pilosa=distribucion_pilosa,lesiones=lesiones,
        faneras=faneras,t_c_subcutaneo=t_c_subcutaneo,estado=True,examen_fisico_id=examen_fisico_id)

        db.session.add(nuevo_pftcs)
        db.session.commit()

        return piel_faneras_tejido_celular_subcutaneo_schema.jsonify(nuevo_pftcs)
    except Exception as e:

        return jsonify({'Error':e})

@pftcs_blueprint.route('/pftcs',methods=['GET'])
def obtener_pftcss():
    pftcs = Piel_Faneras_Tejido_Celular_Subcutaneo.query.filter_by(estado=True)
    resultado = piel_faneras_tejido_celular_subcutaneo_schemas.dump(pftcs)

    return jsonify(resultado)

@pftcs_blueprint.route('/pftcs/<int:id>',methods=['GET'])
def obtener_pftcs(id):
    pftcs = Piel_Faneras_Tejido_Celular_Subcutaneo.query.get_or_404(int(id))
    if pftcs.estado != False:
        return piel_faneras_tejido_celular_subcutaneo_schema.jsonify(pftcs)

@pftcs_blueprint.route('/pftcs/<int:id>',methods=['PUT'])
def actualizar_pftcs(id):
    pftcs = Piel_Faneras_Tejido_Celular_Subcutaneo.query.get_or_404(int(id))

    aspecto= request.json['aspecto']
    distribucion_pilosa= request.json['distribucion_pilosa']
    lesiones= request.json['lesiones']
    faneras= request.json['faneras']
    t_c_subcutaneo= request.json['t_c_subcutaneo']

    pftcs.aspecto = aspecto
    pftcs.distribucion_pilosa = distribucion_pilosa
    pftcs.lesiones = lesiones
    pftcs.faneras = faneras
    pftcs.t_c_subcutaneo = t_c_subcutaneo

    db.session.commit()

    return piel_faneras_tejido_celular_subcutaneo_schema.jsonify(pftcs)

@pftcs_blueprint.route('/pftcs/<int:id>',methods=['DELETE'])
def eliminar_pftcs(id):
    pftcs = Piel_Faneras_Tejido_Celular_Subcutaneo.query.get_or_404(int(id))

    estado = False
    pftcs.estado = estado 
    db.session.commit()

    return piel_faneras_tejido_celular_subcutaneo_schema.jsonify(pftcs)
