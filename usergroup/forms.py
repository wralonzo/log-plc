from django import forms

from usergroup.models import FailureType, Group, GroupEmail

class GroupCreateForm(forms.ModelForm):
    name = forms.CharField(required=True,
                                label="Nombre *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}))
    key = forms.CharField(required=True,
                                label="Identificador del grupo *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese identificador'}))
    
    class Meta:
        model = Group
        fields = '__all__'
        
class FailureTypeCreateForm(forms.ModelForm):
    name = forms.CharField(required=True,
                                label="Nombre *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}))
    
    class Meta:
        model = FailureType
        fields = '__all__'
        
class GroupEmailCreateForm(forms.ModelForm):
    key = forms.CharField(required=True,
                                label="Key del grupo *",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el identificador'}))
    
    class Meta:
        model = GroupEmail
        fields = '__all__'