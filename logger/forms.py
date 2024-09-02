from django import forms

from logger.models import Logger

class LoggerCreateForm(forms.ModelForm):
    description = forms.CharField(required=True,
                                label="Descripciòn *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese descripción de la lectura'}))
    
    operador = forms.CharField(required=True,
                                label="Operador *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese operador'}))
    class Meta:
        model = Logger
        fields = '__all__'