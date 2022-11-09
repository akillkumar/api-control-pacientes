from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Piel_Faneras_Tejido_Celular_SubcutaneoSchema(ma.Schema):
    class Meta:
        fields=('id','aspecto','distribucion_pilosa','lesiones','faneras','t_c_subcutaneo',
        'estado','fecha_creacion','examen_fisico_id')

piel_faneras_tejido_celular_subcutaneo_schema = Piel_Faneras_Tejido_Celular_SubcutaneoSchema(many=False)
piel_faneras_tejido_celular_subcutaneo_schemas = Piel_Faneras_Tejido_Celular_SubcutaneoSchema(many=True)
