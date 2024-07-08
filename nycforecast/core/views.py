from typing import Any
from django.shortcuts import render,redirect
from django.views import View
from .models import City,Prediction
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import PredictionForm
from bs4 import BeautifulSoup
import requests

def get_city_photo(city_name):
    url = "https://www.google.com/search?sca_esv=04aa412ff406bf20&sca_upv=1&q={}&udm=2".format(city_name)
    r = requests.get(url)
    txt = r.text

    soup = BeautifulSoup(r.content,'html.parser')

    elements = soup.find_all('img')

    return elements[1]['src']


class IndexView(View):
    def get(self,request):
        lst = Prediction.objects.all()
        return render(request,'core/home.html',{'predictions':lst})

class PredictionDetailView(DetailView):
    model = Prediction
    template_name = 'core/prediction.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CityDetailView(DetailView):
    model = City
    template_name = 'core/city.html'

    def get_context_data(self, **kwargs: Any):
        return super().get_context_data(**kwargs)

def deleteView(request,id):
    obj = Prediction.objects.get(id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    template_name = 'core/confirm.html'
    context = {'obj' : obj}
    return render(request,template_name,context)


class CityListView(ListView):
    model = City
    template_name = 'core/cities.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cities_all = City.objects.all()

       
        return context

class NewPredictionView(View):
    def get(self,request):
        new_form = PredictionForm()
        return render(request,'core/newprediction.html',{'form' : new_form})
    def post(self,request):
        new_form = PredictionForm(request.POST)
        if new_form.is_valid():
            new_form.save()
        return redirect('home')
        


