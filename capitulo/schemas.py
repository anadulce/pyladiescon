from ninja import Field, ModelSchema
from .models import Capitulo, PyLady



class CapituloSchema(ModelSchema):
    class Meta:
        model = Capitulo
        exclude = ["id", "slug"]


class ListaCapituloSchema(ModelSchema):
    numero_de_integrantes: int = Field(..., alias="numero_de_integrantes")
    class Meta:
        model = Capitulo
        exclude = ["id"]


class PyLadySchema(ModelSchema):
    class Meta:
        model = PyLady
        exclude = ["id", "capitulo"]