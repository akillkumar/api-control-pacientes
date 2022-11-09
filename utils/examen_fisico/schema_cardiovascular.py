from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CardiovascularSchema(ma.Schema):
    class Meta:
        fields=('id','inspeccion','palpacion','auscultacion','pulsos','estado','fecha_creacion','examen_fisico_id')

cardiovascular_schema=CardiovascularSchema(many=False)
cardiovascular_schemas=CardiovascularSchema(many=True)