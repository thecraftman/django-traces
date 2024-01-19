from django.http import HttpResponse
from random import randint
from .exporter import tracer  # Import the tracer

def roll_dice(request):
    with tracer.start_as_current_span("roll_dice_span"):
        result = randint(1, 6)
        return HttpResponse(str(result))

def home(request):
    with tracer.start_as_current_span("home_span"):
        return HttpResponse("Welcome to the homepage axiom!")


# Create your views here.
