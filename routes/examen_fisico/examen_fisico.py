from models.model import *
from utils.examen_fisico.schema_examen_fisico import *
from flask import  jsonify, request, Blueprint


examen_fisico_blueprint = Blueprint('examen_fisico',__name__)

@examen_fisico_blueprint.route('/examen_fisico',methods=['POST'])
def crear_examen_fisico():
    try:
        ta= request.json['ta']
        fc= request.json['fc']
        fr= request.json['fr']
        temperatura= request.json['temperatura']
        altura= request.json['altura']
        peso= request.json['peso']
        impresion_general= request.json['impresion_general']
        constitucion= request.json['constitucion']
        facies= request.json['facies']
        actitud= request.json['actitud']
        decubito= request.json['decubito']
        marcha= request.json['marcha']
        consulta_id= request.json['consulta_id']

        nuevo_examen_fisico = Examen_Fisico(ta=ta,fc=fc,fr=fr,temperatura=temperatura,altura=altura,peso=peso,
        impresion_general=impresion_general,constitucion=constitucion,facies=facies,actitud=actitud,
        decubito=decubito,marcha=marcha,estado=True,consulta_id=consulta_id)

        db.session.add(nuevo_examen_fisico)
        db.session.commit()

        return examen_fisico_schema.jsonify(nuevo_examen_fisico)
    except Exception as e:

        return jsonify({'Error':e})

@examen_fisico_blueprint.route('/examen_fisico',methods=['GET'])
def obtener_examenes_fisicos():
    examen_fisico = Examen_Fisico.query.filter_by(estado=True)

    resultado = examen_fisico_schemas.dump(examen_fisico)

    return jsonify(resultado)


@examen_fisico_blueprint.route('/examen_fisico/<int:id>',methods=['GET'])
def obtener_examen_fisico(id):
    examen_fisico = Examen_Fisico.query.get_or_404(int(id))
    if(examen_fisico.estado != False):
        return examen_fisico_schema.jsonify(examen_fisico)
    else:
        return "<h1>No existe el examen fisico.</h1>"
        


@examen_fisico_blueprint.route('/examen_fisico/<int:id>',methods=['PUT'])
def actualizar_examen_fisico(id):
    examen_fisico = Examen_Fisico.query.get_or_404(int(id))

    ta= request.json['ta']
    fc= request.json['fc']
    fr= request.json['fr']
    temperatura= request.json['temperatura']
    altura= request.json['altura']
    peso= request.json['peso']
    impresion_general= request.json['impresion_general']
    constitucion= request.json['constitucion']
    facies= request.json['facies']
    actitud= request.json['actitud']
    decubito= request.json['decubito']
    marcha= request.json['marcha']

    examen_fisico.ta = ta
    examen_fisico.fc = fc
    examen_fisico.fr = fr
    examen_fisico.temperatura = temperatura
    examen_fisico.altura = altura
    examen_fisico.peso = peso
    examen_fisico.impresion_general = impresion_general 
    examen_fisico.constitucion = constitucion
    examen_fisico.facies = facies
    examen_fisico.actitud = actitud
    examen_fisico.decubito = decubito
    examen_fisico.marcha = marcha

    db.session.commit()

    return examen_fisico_schema.jsonify(examen_fisico)

@examen_fisico_blueprint.route('/examen_fisico/<int:id>',methods=['DELETE'])
def elimiar_examen_fisico(id):
    examen_fisico = Examen_Fisico.query.get_or_404(int(id))
    estado = False
    examen_fisico.estado = estado 
    db.session.commit()

    return examen_fisico_schema.jsonify(examen_fisico)

