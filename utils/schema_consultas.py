from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ConsultasSchema(ma.Schema):
    class Meta:
        fields=('id','motivo_consulta','enfermedad_actual','antecedentes_enfermedad_ac',
        'antecedentes_familiares','fecha_consulta','estado','fecha_creacion','paciente_id')


consulta_Schema=ConsultasSchema(many=False)
consultas_Schema=ConsultasSchema(many=True)
