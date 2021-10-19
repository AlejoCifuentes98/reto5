from apps.portafolio.models import *
from .serializer import *
from rest_framework import viewsets

class categoria_viewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoria_serializer 
class proyectos_viewset(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    serializer_class = proyecto_serializer 
