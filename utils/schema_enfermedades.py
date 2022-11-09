from flask_marshmallow import Marshmallow

ma = Marshmallow()

class EnfermedadesSchema(ma.Schema):
    class Meta:
        fields=('id','cv','respiratorio','nefrourologicos','hematologicos','infectologicos','endocrinologicos',
        'quirurgicos','traumatologicos','alergicos','epidemiologicos','antecedentes_heredofamilaires',
        'estado','fecha_creacion','consulta_id')

enfermedades_schema = EnfermedadesSchema(many=False)
enfermedades_schemas = EnfermedadesSchema(many=True)