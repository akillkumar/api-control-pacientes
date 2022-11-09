from flask_marshmallow import Marshmallow

ma = Marshmallow()

class PacientesSchema(ma.Schema):
    class Meta:
        fields=('id','identificacion','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido',
        'genero','fecha_nacimiento','telefono','correo','ocupacion','estado','fecha_creacion','medico_id')





paciente_schema = PacientesSchema(many=False)
pacientes_schema = PacientesSchema(many=True)



