from django.shortcuts import render
from about_us.models import About


def AboutView(request):
    return render(request, "about_us/about_us.html", {"About_us": About.objects.all()})
