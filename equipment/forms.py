from django import forms
from equipment.models import Device, Sensor

class DeviceCreateForm(forms.ModelForm):
    name = forms.CharField(required=True,
                                label="Nombre del PLC *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}))
    location = forms.CharField(required=True,
                                label="Ubicación del PLC *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ubicación'}))
    encargado = forms.CharField(required=True,
                                label="Encargado del PLC *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del encargado'}))
    class Meta:
        model = Device
        fields = '__all__'
        

class SensorCreateForm(forms.ModelForm):
    name = forms.CharField(required=True,
                                label="Nombre del sensor *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}))
    widgets = {
            'deviceId': forms.Select(attrs={'class': 'form-control'}),
        }
    class Meta:
        model = Sensor
        fields = '__all__'