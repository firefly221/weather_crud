from django.urls import path
from .views import IndexView,PredictionDetailView,CityDetailView,deleteView,CityListView,NewPredictionView


urlpatterns = [
    path('home/',IndexView.as_view(),name='home'),
    path('prediction/<int:pk>/',PredictionDetailView.as_view(),name="prediction"),
    path('city/<int:pk>/',CityDetailView.as_view(),name='city'),
    path('delete/<int:id>',deleteView,name="del"),
    path('cities/',CityListView.as_view(),name='cities'),
    path('newprediction/',NewPredictionView.as_view(),name='newpred')
]












