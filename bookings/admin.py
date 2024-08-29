from django.contrib import admin
from .models import Booking, Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('number',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'guests', 'special_requests', 'user', 'table')
    list_filter = ('date', 'time', 'table')
    search_fields = ('special_requests',)