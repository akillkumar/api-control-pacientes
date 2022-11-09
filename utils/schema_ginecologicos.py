from flask_marshmallow import Marshmallow

ma = Marshmallow()


class GinecologicosSchema(ma.Schema):
    class Meta:
        fields=('id','e','p','c','a','mac','fum','menarca','menopausia','estado','fecha_creacion','enfermedades_id')


ginecologicos_schema=GinecologicosSchema(many=False)
ginecologicos_schemas=GinecologicosSchema(many=True)