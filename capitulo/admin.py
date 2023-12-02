from django.contrib import admin


from .models import Capitulo, PyLady


@admin.register(Capitulo)
class CapituloAdmin(admin.ModelAdmin):
    ...


@admin.register(PyLady)
class PyLadyAdmin(admin.ModelAdmin):
    ...