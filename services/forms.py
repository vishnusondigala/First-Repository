from django import forms
from .models import Servicee

class serviceForm (forms.ModelForm):
    class Meta:
        model = Servicee
        fields = '__all__' 
