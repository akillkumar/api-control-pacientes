from flask_marshmallow import Marshmallow

ma = Marshmallow()


class SensibilidadSuperficialSchema(ma.Schema):
    class Meta:
        fields=('id','tactil','dolorosa','termica','estado','fecha_creacion','neurologico_id')


sensibilidad_superficial_schema = SensibilidadSuperficialSchema(many=False)
sensibilidad_superficial_schemas = SensibilidadSuperficialSchema(many=True)
 