from django.urls import path, include
from .import views


app_name = "main"

urlpatterns = [
    path('', views.IndexView, name='home'),
    path('region/<int:country_id>/', views.CountriesView, name='region'),
    path('search/', views.SearchView, name='search'),
]
