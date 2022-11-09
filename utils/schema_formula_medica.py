from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Formula_MedicaSchema(ma.Schema):
    class Meta:
        fields=('id','preescribe','recomendacion','fecha_inicio','fecha_fin','observaciones','estado',
        'fecha_cracion','paciente_id')

formula_medica_schema = Formula_MedicaSchema(many=False)
formula_medica_schemas = Formula_MedicaSchema(many=True)