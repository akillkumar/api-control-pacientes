from flask_marshmallow import Marshmallow

ma = Marshmallow()

class MedicamentosSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','cantidad','estado','fecha_creacion','formula_medica_id')

medicamentos_schema = MedicamentosSchema(many=False)
medicamentos_schemas = MedicamentosSchema(many=True)