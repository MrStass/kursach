from django.urls import path
from .import views


app_name = "about_us"

urlpatterns = [
    path('about/', views.AboutView, name='about-us'),
]
