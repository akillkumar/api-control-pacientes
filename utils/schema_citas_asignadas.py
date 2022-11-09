from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Citas_AsignadasSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','hora','estado','fecha_creacion','paciente_id','solicitud_cita_paciente_id')


citas_asignadas_schema = Citas_AsignadasSchema(many=False)
citas_asignadas_schemas = Citas_AsignadasSchema(many=True)