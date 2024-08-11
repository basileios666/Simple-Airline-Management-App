from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from flights import models

def index(request):
    return render(request, "flights/index.html", {
        "flights": models.Flight.objects.all()
    })

def flight(request, flight_id):
    flight = models.Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_pass": models.Passenger.objects.exclude(flights = flight).all(),
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = models.Flight.objects.get(pk=flight_id)
        passenger = models.Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))