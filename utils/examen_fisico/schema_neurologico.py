from flask_marshmallow import Marshmallow

ma = Marshmallow()

class NeurologicoSchema(ma.Schema):
    class Meta:
        fields=('id','glasgow','motilidad_activa','motilidad_refleja','motilidad_pasiva','pares_craneales',
        'estado','fecha_creacion','examen_fisico_id')

neurologico_schema = NeurologicoSchema(many=False)
neuorlogico_schemas = NeurologicoSchema(many=True)