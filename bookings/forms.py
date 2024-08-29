from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.filter(is_available=True))

    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'guests', 'special_requests']