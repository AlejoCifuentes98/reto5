from rest_framework import serializers
from apps.portafolio.models import *

class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre',)

class proyecto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyectos
        fields = ('url', 'titulo','descripcion','fecha_creacion','imagen','categoria',)


