from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Categoria, Proyectos 
from .forms import proyecto_agregar_form, categoria_agregar_form, login_form, registro_form
from django.contrib.auth.decorators import login_required


def inicio_view(request):
    cards= Proyectos.objects.filter()
    return render(request,'portafolio/inicio.html', locals()) 

def detalles_view(request, id_proyecto):
    card = Proyectos.objects.get(id=id_proyecto)
    return render(request, 'portafolio/detalles.html', locals())

def login_view(request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario =authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/inicio_admin/')
            else:
                msj = 'Sus credenciales son incorrectas, verifique e intente nuevamente.'
    formulario = login_form()
    return render (request, 'admin/login.html', locals())

def registro_view(request):

    if request.method == 'POST':
        form_u = registro_form(request.POST) 
        if form_u.is_valid():
            correo =  form_u.cleaned_data['correo']
            clave_1 = form_u.cleaned_data['clave_1']
            clave_2 = form_u.cleaned_data['clave_2']
            u = User.objects.create_user(username= correo, password= clave_2, is_superuser=True, is_staff=True) 
            u.save()       
            return redirect ('/login/')
    else:  
        form_u = registro_form()
        return render(request, 'admin/registro.html', locals())
    return render(request, 'admin/registro.html', locals())

def logout_view(request):
    logout(request)
    return redirect ('/login/')

@login_required
def inicio_admin_view(request):
    proyectos= Proyectos.objects.filter()
    return render(request, 'admin/inicio_admin.html', locals())

@login_required
def proyecto_agregar_view(request):
    categorias= Categoria.objects.filter()
    if request.method == 'POST':
        formulario = proyecto_agregar_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/inicio_admin/')
    else:
        formulario = proyecto_agregar_form()
        
    return render(request, 'admin/proyecto_agregar.html', locals())

@login_required
def proyecto_editar_view(request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    if request.method == 'GET':
        formulario = proyecto_agregar_form(instance=proyecto)
    else:
        formulario = proyecto_agregar_form(request.POST, instance=proyecto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/inicio_admin/')    
    return render(request, 'admin/proyecto_editar.html', locals())

@login_required
def proyecto_eliminar_view(request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    if request.method =='POST':
        proyecto.delete()
        return redirect('/inicio_admin/')
    return render(request, 'admin/proyecto_eliminar.html', locals())

@login_required
def categorias_view(request):
    categorias= Categoria.objects.filter()
    return render(request, 'admin/categorias.html', locals())

@login_required
def categoria_agregar_view(request):
    if request.method == 'POST':
        formulario = categoria_agregar_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/categorias/')
    else:
        formulario = categoria_agregar_form()
    return render(request, 'admin/categoria_agregar.html', locals())

@login_required
def categoria_editar_view(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'GET':
        formulario = categoria_agregar_form(instance=categoria)
    else:
        formulario = categoria_agregar_form(request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('/categorias/')    
    return render(request, 'admin/categoria_editar.html', locals())

@login_required
def categoria_eliminar_view(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method =='POST':
        categoria.delete()
        return redirect('/categorias/')
    return render(request, 'admin/categoria_eliminar.html', locals())

