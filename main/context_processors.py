from .models import Region

def extras(request):
    region = Region.objects.all()
    return {"Regions": region}
