from django.urls import path
from .views import Home, TimeTable, Stations, Reservation


urlpatterns = [
path('', Home.as_view(), name='home'),
path('timetables', TimeTable.as_view(), name='timetables'),
path('stations', Stations.as_view(), name='stations'),
path('reservations', Reservation.as_view(), name='reservations'),
   
]
