from flask_marshmallow import Marshmallow

ma = Marshmallow()

class SchemaExamenFisico(ma.Schema):
    class Meta:
        fields=('id','ta','fc','fr','temperatura','altura','peso','impresion_general','constitucion','facies',
        'actitud','decubito','marcha','estado','fecha_creacion','consulta_id')


examen_fisico_schema = SchemaExamenFisico(many=False)
examen_fisico_schemas = SchemaExamenFisico(many=True)