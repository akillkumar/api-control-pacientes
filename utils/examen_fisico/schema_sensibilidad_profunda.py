from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Sensibilidad_ProfundaSchema(ma.Schema):
    class Meta:
        fields=('id','dolor_profunda','vibratoria','estado','fecha_creacion','neurologico_id')

sensibilidad_profunda_schema = Sensibilidad_ProfundaSchema(many=False)
sensibilidad_profunda_schemas = Sensibilidad_ProfundaSchema(many=True)         