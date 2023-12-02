from typing import List

from ninja import Header, Router
from slugify import slugify

from .models import Capitulo, PyLady
from .schemas import CapituloSchema, ListaCapituloSchema, PyLadySchema

router = Router()

@router.post(
    "/capitulo", 
    response=CapituloSchema, 
    tags=["Capitulos"], 
    url_name="criar_capitulo",
)
def criar_capitulo(request, data: CapituloSchema):
    entrada = data.dict()
    entrada["slug"] = slugify("")
    capitulo = Capitulo.objects.create(**data.dict())
    return capitulo


@router.get(
    "/capitulo", 
    response=List[ListaCapituloSchema], 
    tags=["Capitulos"], 
    url_name="listar_capitulo",
)
def listar_capitulo(request):
    return Capitulo.objects.all()

@router.post(
    "/{capitulo}/pylady", 
    response=PyLadySchema, 
    tags=["PyLadies"], 
    url_name="criar_pylady",
)
def criar_pylady(request, capitulo: str, data: PyLadySchema):
    entrada = data.dict()
    entrada["capitulo"] = Capitulo.objects.get(slug=capitulo)
    pylady = PyLady.objects.create(**entrada)
    return pylady

@router.get(
    "/{capitulo}/pylady", 
    response=List[PyLadySchema], 
    tags=["PyLadies"], 
    url_name="listar_pyladies",
)
def listar_pyladies(request, capitulo: str):
    capitulo = Capitulo.objects.get(slug=capitulo)
    return capitulo.integrantes.all()