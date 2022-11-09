from flask_marshmallow import Marshmallow

ma = Marshmallow()

class AbdomenSchema(ma.Schema):
    class Meta:
        fields=('id','inspeccion','palpacion','percusion','auscultacion','estado','fecha_creacion','examen_fisico_id')

abdomen_schema=AbdomenSchema(many=False)
abdomen_schemas=AbdomenSchema(many=True)