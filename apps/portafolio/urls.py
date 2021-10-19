from django.urls import path
from .views import inicio_view,detalles_view, inicio_admin_view, proyecto_agregar_view, proyecto_editar_view, proyecto_eliminar_view, categorias_view, categoria_agregar_view, categoria_editar_view, categoria_eliminar_view, login_view, registro_view, logout_view

urlpatterns = [
    path("", inicio_view, name='inicio'),
    path("detalles/<int:id_proyecto>/", detalles_view, name='detalles'),

    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("registro/", registro_view, name="registro"),

    path("inicio_admin/", inicio_admin_view, name='inicio_admin'),
    path("proyecto_agregar/", proyecto_agregar_view, name='proyecto_agregar'),
    path("proyecto_editar/<int:id_proyecto>/", proyecto_editar_view, name='proyecto_editar'),
    path("proyecto_eliminar/<int:id_proyecto>/", proyecto_eliminar_view, name='proyecto_eliminar'),

    path("categorias/", categorias_view, name='categorias'),
    path("categoria_agregar/", categoria_agregar_view, name='categoria_agregar'),
    path("categoria_editar/<int:id_categoria>/", categoria_editar_view, name='categoria_editar'),
    path("categoria_eliminar/<int:id_categoria>/", categoria_eliminar_view, name='categoria_eliminar'),
   

]