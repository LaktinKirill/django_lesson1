from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def data(request):
    return HttpResponse("<h1>Моя первая страничка Джанго</h1>")

def test(request):
    return HttpResponse("<h1>Новая текстовая страница</h1>")
