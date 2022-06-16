from django.core.paginator import Paginator
from .models import Region, Country
from django.shortcuts import render
from attractions.models import Attractions

def IndexView(request):
    return render(request, "main/index.html", {"Regions": Region.objects.all()})


def CountriesView(request, country_id):
    p = Paginator(Country.objects.filter(region=country_id), 4)
    page = request.GET.get('page')
    countries = p.get_page(page)
    return render(request, "main/countries.html", {"Countries": countries})



def SearchView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        attractions_by_name = Attractions.objects.filter(title__icontains=searched)
        attractions_by_country = Attractions.objects.filter(country__title__icontains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'attractions':  attractions_by_name if attractions_by_name else attractions_by_country})
    else:
        return render(request, 'main/search.html', {})
