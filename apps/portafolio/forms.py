from django import forms
from django.contrib.auth.models import User
from .models import Proyectos, Categoria



class categoria_agregar_form (forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super(categoria_agregar_form, self).__init__(*args, **kwargs)
        for field in self.fields:	
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            

class proyecto_agregar_form (forms.ModelForm):
    fecha_creacion = forms.DateField(label='Fecha de creacion', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=True)
    class Meta:
        model = Proyectos
        fields = '__all__'
        
    
    def __init__(self, *args, **kwargs):
        super(proyecto_agregar_form, self).__init__(*args, **kwargs)
        for field in self.fields:	
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class categoria_agregar_form (forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(categoria_agregar_form, self).__init__(*args, **kwargs)
        for field in self.fields:	
            self.fields[field].widget.attrs.update({'class': 'form-control'})    
        
    
    
            
class login_form (forms.Form):
    

    usuario = forms.CharField(widget=forms.TextInput())  
    clave   = forms.CharField(widget=forms.PasswordInput(render_value=False))  

class registro_form (forms.Form):
    correo    = forms.EmailField(label='Ingrese su correo', widget= forms.TextInput(attrs={'class':'form-control'}))
    clave_1  = forms.CharField(label='Ingrese su contraseña', widget= forms.PasswordInput(attrs={'class':'form-control'},render_value= False))
    clave_2  = forms.CharField(label='Confirme la contraseña', widget= forms.PasswordInput(attrs={'class':'form-control'}, render_value= False))


    def clean_username(self):
        correo = self.cleaned_data['correo']
        try:
            c = User.objects.get(username = correo)
        except User.DoesNotExist:
            return correo
        raise forms.ValidationError('El correo ingresado, ya se encuentra registrado')
            
 