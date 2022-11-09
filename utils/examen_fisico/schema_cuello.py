from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CuelloSchema(ma.Schema):
    class Meta:
        fields=('id','inspeccion','palpacion','percusion','auscultacion','estado','fecha_creacion','examen_fisico_id')

cuello_schema=CuelloSchema(many=False)
cuello_schemas=CuelloSchema(many=True)