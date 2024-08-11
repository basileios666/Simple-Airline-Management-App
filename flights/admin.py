from django.contrib import admin

class FlightAdmin(admin.ModelAdmin):
    list_display = ("__str__", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

# Register your models here.
from flights import models

admin.site.register(models.Flight, FlightAdmin)
admin.site.register(models.Airport)
admin.site.register(models.Passenger, PassengerAdmin)