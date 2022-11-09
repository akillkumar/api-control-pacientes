from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Antecedentes_PersonalesSchema(ma.Schema):
    class Meta:
        fields=('id','enfermedad_de_infancia','estado','fecha_creacion','consulta_id')


antecedentes_personales_schema= Antecedentes_PersonalesSchema(many=False)
antecedentes_personales_schemas= Antecedentes_PersonalesSchema(many=True)