from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        # Проверка на новое бронирование
        if self.pk is None:
            if not self.table.is_available:
                raise ValueError("The selected table is not available.")
            if Booking.objects.filter(date=self.date, time=self.time, table=self.table).exists():
                raise ValueError("The selected table is already booked for this time.")
            if self.guests > self.table.capacity:
                raise ValueError("The number of guests exceeds the table capacity.")

        super().save(*args, **kwargs)

        # Обновление статуса доступности столика после успешного бронирования
        if self.status == 'confirmed':
            self.table.is_available = False
            self.table.save()

    def __str__(self):
        return f"Booking for Table {self.table.number} on {self.date} at {self.time}"
