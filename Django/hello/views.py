from django.http import HttpResponse

def home(request):
    return HttpResponse("Heelo, This is my first django app")

# Create your views here.
