from .models import Region, Country
from django.shortcuts import render
from attractions.models import Attractions

def IndexView(request):
    return render(request, "main/index.html", {"Regions": Region.objects.all()})


def CountriesView(request, country_id):
    return render(request, "main/countries.html", {"Countries": Country.objects.filter(region=country_id)})


def SearchView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        attractions_by_name = Attractions.objects.filter(title__icontains=searched)
        attractions_by_country = Attractions.objects.filter(country__title__icontains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'attractions':  attractions_by_name if attractions_by_name else attractions_by_country})
    else:
        return render(request, 'main/search.html', {})
