from django.shortcuts import render
from .models import Greeting, Visit  # <-- DODANO Visit

# Create your views here.

def index(request):
    # Zapis każdej wizyty w bazie
    Visit.objects.create()         # <-- DODANO TĘ LINIĘ
    
    # Pobranie liczby wszystkich wizyt
    visits = Visit.objects.count()  # <-- DODANO TĘ LINIĘ
    
    # Przekazanie liczby wizyt do szablonu index.html
    return render(request, "index.html", {"visits": visits})  # <-- DODANO {"visits": visits}


def db(request):
    # Tę funkcję zostawiamy bez zmian, tak jak była w oryginale
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})