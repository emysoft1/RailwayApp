from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, View,ListView,FormView
from railwayApp.models import Train, Station
from .forms import ReservationForm
from django.urls import reverse_lazy
# Create your views here.


class Home(TemplateView):
    template_name = "index.html"



class TimeTable(ListView):
    template_name = "timetable.html"
    model = Train


class Stations(ListView):
    model = Station
    template_name = 'stations.html'
   


class Reservation(SuccessMessageMixin,FormView):
    form_class = ReservationForm
    template_name = "reservation.html"
    success_url = reverse_lazy('reservations')
    success_message = "Your Reservation was successfully!"

    def form_valid(self, form):
        form.save()
        return super(Reservation, self).form_valid(form)
