from flask_marshmallow import Marshmallow

ma = Marshmallow()

class CabezaSchema(ma.Schema):
    class Meta:
        fields=('id','craneo_y_cara','cuero_cabelludo','region_frontal','region_obitonasal','region_orinfarengea',
        'estado','fecha_creacion','examen_fisico_id')

cabeza_schema = CabezaSchema(many=False)
cabeza_schemas= CabezaSchema(many=True)