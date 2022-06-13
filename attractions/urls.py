from django.urls import path
from .import views


app_name = "attractions"

urlpatterns = [
    path('country/<int:attractions_id>', views.AttractionsView, name='attractions'),
]
