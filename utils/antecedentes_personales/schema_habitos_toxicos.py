from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Habitos_ToxicosSchema(ma.Schema):
    class Meta:
        fields=('id','alcohol','tabaco','drogas','infusiones','estado','fecha_creacion','antecedentes_personales_id')


habitos_toxicos_schema = Habitos_ToxicosSchema(many=False)
habitos_toxicos_schemas = Habitos_ToxicosSchema(many=True) 