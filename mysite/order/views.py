from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def detail(request, date_id):
    return HttpResponse("Wybrany Kontener %s." % date_id)