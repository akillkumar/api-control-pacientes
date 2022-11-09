from platform import mac_ver
from tkinter import E
from models.model import *
from utils.schema_ginecologicos import *
from flask import  jsonify, request, Blueprint

ginecologicos_blueprint = Blueprint('ginecologicos',__name__)

@ginecologicos_blueprint.route('/ginecologicos',methods=['POST'])
def crear_ginecologicos():
    try:
        e = request.json['e']
        p = request.json['p']
        c = request.json['c']
        a = request.json['a']
        mac = request.json['mac']
        fum = request.json['fum']
        menarca = request.json['menarca']
        menopausia = request.json['menopausia']
        enfermedades_id = request.json['enfermedades_id']

        nuevo_ginecologicos = Ginecologicos(e=e,p=p,c=c,a=a,mac=mac,fum=fum,menarca=menarca,
        menopausia=menopausia,estado=True,enfermedades_id=enfermedades_id)

        db.session.add(nuevo_ginecologicos)
        db.session.commit()

        return ginecologicos_schema.jsonify(nuevo_ginecologicos)
    except Exception as e:
        return jsonify({'errrr':e})


@ginecologicos_blueprint.route('/ginecologicos',methods=['GET'])
def obtener_ginecologicos():
    ginecologicos = Ginecologicos.query.filter_by(estado=True)
    resultado = ginecologicos_schemas.dump(ginecologicos)
    return jsonify(resultado)
@ginecologicos_blueprint.route('/ginecologicos/<int:id>',methods=['GET'])
def obtenr_ginecologico(id):
    ginecologico = Ginecologicos.query.get_or_404(int(id))
    if ginecologico.estado != False:
        return ginecologicos_schema.jsonify(ginecologico)
    else:
        return '<h1>no se encuentra ginecologico </h1>'
@ginecologicos_blueprint.route('/ginecologicos/<int:id>',methods=['PUT'])
def actualizar_ginecologico(id):
    ginecologico = Ginecologicos.query.get_or_404(int(id))

    e = request.json['e']
    p = request.json['p']
    c = request.json['c']
    a = request.json['a']
    mac = request.json['mac']
    fum = request.json['fum']
    menarca = request.json['menarca']
    menopausia = request.json['menopausia']

    ginecologico.e =e
    ginecologico.p =p
    ginecologico.c =c
    ginecologico.a =a
    ginecologico.mac =mac
    ginecologico.fum =fum
    ginecologico.menarca =menarca
    ginecologico.menopausia =menopausia

    db.session.commit()

    return ginecologicos_schema.jsonify(ginecologico)

@ginecologicos_blueprint.route('/ginecologicos/<int:id>',methods=['DELETE'])
def eliminar_ginecologico(id):
    ginecologico = Ginecologicos.query.get_or_404(int(id))
    estado = False
    ginecologico.estado = estado
    db.session.commit()
    return jsonify({'Mensaje':'Se ha eliminado con exito!'})