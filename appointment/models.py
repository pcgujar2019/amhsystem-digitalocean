from django.db import models
from django.db.models.fields import TimeField
from main.models import Patient

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)
    on_date = models.DateField(blank=False)
    visit_no = models.IntegerField(blank=True, null=True)
    # at_time = models.TimeField(blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True)