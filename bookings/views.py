from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            table = booking.table

            if table is None:
                form.add_error(None, 'Table is not selected.')
            else:
                existing_bookings = Booking.objects.filter(
                    date=booking.date,
                    time=booking.time,
                    table=table
                )
                if existing_bookings.exists():
                    form.add_error(None,
                                   'The selected table is already booked for this time. Please choose a different table or time.')
                elif booking.guests > table.capacity:
                    form.add_error(None, 'The number of guests exceeds the table capacity.')
                else:
                    booking.save()
                    return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'bookings/book_table.html', {'form': form})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/edit_booking.html', {'form': form})




@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('profile')
    return render(request, 'bookings/delete_booking.html', {'booking': booking})


def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})