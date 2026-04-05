from django.db import models
from django.utils import timezone
from patients.models import Patient
from staff.models import Staff


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]

    TYPE_CHOICES = [
        ('general', 'General Checkup'),
        ('followup', 'Follow Up'),
        ('emergency', 'Emergency'),
        ('specialist', 'Specialist'),
        ('lab', 'Lab Test'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='general')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    reason = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return f"{self.patient} — Dr.{self.doctor} — {self.appointment_date}"

    @property
    def is_upcoming(self):
        return self.appointment_date >= timezone.now().date()

    @property
    def is_overdue(self):
        return self.appointment_date < timezone.now().date() and self.status == 'scheduled'