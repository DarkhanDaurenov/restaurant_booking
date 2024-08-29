from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_table, name='book_table'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]