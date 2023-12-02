from ninja import NinjaAPI
from capitulo.views import router

api = NinjaAPI()

api.add_router("/", router)