from django.urls import path, include
from rest_framework import routers
from apps.portafolio.models import *
from .views import * 

router = routers.DefaultRouter()
router.register(r'proyectos', proyectos_viewset)
router.register(r'categoria', categoria_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
