from django.http import HttpResponseRedirect

from .models import Attractions
from django.shortcuts import render, get_object_or_404


def AttractionsView(request, attractions_id):
    return render(request, "attractions/attractions_list.html", {"Attractions": Attractions.objects.filter(country=attractions_id)})


