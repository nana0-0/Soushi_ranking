from django.shortcuts import render
from .models import Person

# Create your views here.


def index(request):
    persons = Person.objects.order_by("score").reverse()[:5]
    return render(request, "ranking/index.html", {"persons": persons})
