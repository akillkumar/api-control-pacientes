from flask_marshmallow import Marshmallow

ma = Marshmallow()

class RespiratorioSchema(ma.Schema):
    class Meta:
        fields=('id','inspeccion','palpacion','percusion','auscultacion','estado','fecha_creacion','examen_fisico_id')

respiratorio_schema=RespiratorioSchema(many=False)
respiratorio_schemas=RespiratorioSchema(many=True)