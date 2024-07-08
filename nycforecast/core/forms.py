from django.forms import ModelForm
from .models import Prediction
from django import forms

class PredictionForm(ModelForm):
    class Meta:
        model = Prediction
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['city'].widget.attrs.update({'class' : 'form-control'})


    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    degrees = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    tornado_percent = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    rain_percent = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))












