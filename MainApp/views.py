from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

countries = open("country-by-languages.json", 'r')
# iter_ = len(list(countries))
# i = [i for i in range(1, iter_+1)]

def home(request):
    return render (request, "home_page.html", {})

def countries_list(request):
    context = {
        "countries": countries.read()
        }
    return render(request, "countries_list.html", context)
