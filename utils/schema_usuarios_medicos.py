from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UsuariosMedicosSchema(ma.Schema):
    class Meta:
        fields=('id','identificacion','password','tipo_usuario','estado','fecha_creacion','medico_id')

class JoinUsuariosMedicosConMedico(ma.Schema):
    class Meta:
        fields=('id','identificacion','password','tipo_usuario','estado','fecha_creacion','medico_id','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido',
        'especializacion','estado',)

    
usuarios_medicos_schema = UsuariosMedicosSchema(many=False)
usuarios_medicos_schemas = UsuariosMedicosSchema(many=True)

JoinUsuariosMedicosConMedico_schema = JoinUsuariosMedicosConMedico(many=True)
JoinUsuariosMedicosConMedico_schemas = JoinUsuariosMedicosConMedico(many=False)