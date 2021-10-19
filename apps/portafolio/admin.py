from apps.portafolio.models import Categoria, Proyectos
from django.contrib import admin
from .models import Proyectos, Categoria
admin.site.register(Proyectos)
admin.site.register(Categoria)
