from flask_marshmallow import Marshmallow

ma = Marshmallow()

class MedicosSchema(ma.Schema):
    class Meta:
        fields=('id','identificacion','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido',
        'especializacion','estado','fecha_creacion')

medico_shema = MedicosSchema(many=False)
medicos_shemas = MedicosSchema(many=True)