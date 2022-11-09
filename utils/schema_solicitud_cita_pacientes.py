from dataclasses import field
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class Solicitud_Cita_PacientesSchema(ma.Schema):
    class Meta:
        fields=('id','estado','fecha_creacion','paciente_id')

s_c_p_schema = Solicitud_Cita_PacientesSchema(many=False)
s_c_p_schemas = Solicitud_Cita_PacientesSchema(many=True)