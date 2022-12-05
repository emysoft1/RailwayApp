from django.contrib import admin

from .models import Station, Train, Route, Reservation,Titles


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_of_station',
        'location',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_of_train',
        'train_number',
        'station',
        'route',
        'available_seat',
        'seat_type',
        'departure_time',
        'arrival_time',
        'duration',
    )
    list_filter = ('station',  'route', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source',
        'destination',
        'price',
    )
    list_filter = ('source', 'destination', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'status',
        'no_of_person',
        'gender',
        'ticket_number',
        'Journey',
        'created_at',
        'updated_at',
    )
    list_filter = ( 'Journey', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text_title',
        'sub_title',
    )
    list_filter = ('id','text_title','sub_title')