from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UsuariosPacientesSchema(ma.Schema):
    class Meta:
        fields=('id','identificacion','password','tipo_usuario','estado','fecha_creacion','paciente_id')
    
usuarios_pacientes_schema = UsuariosPacientesSchema(many=False)
usuarios_pacientes_schemas = UsuariosPacientesSchema(many=True)