from .models import Attractions
from django.shortcuts import render


def AttractionsView(request, attractions_id):
    return render(request, "attractions/attractions_list.html", {"Attractions": Attractions.objects.filter(country=attractions_id)})

