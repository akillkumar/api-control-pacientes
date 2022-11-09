from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Habitos_FisiologicosSchema(ma.Schema):
    class Meta:
        fields=('id','alimentacion','diuresis','catarsis','sueño','sexualidad','otros','estado',
        'fecha_creacion','antecedentes_personales_id')

habitos_fisiologicos_schema= Habitos_FisiologicosSchema(many=False)
habitos_fisiologicos_schemas= Habitos_FisiologicosSchema(many=True)