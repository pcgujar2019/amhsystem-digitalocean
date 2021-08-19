from django.db import models
from main.models import Patient

# Create your models here.
class Medicine(models.Model):
    class MedicineForm(models.TextChoices):
        Tablet = 'Tablet'
        Powder = 'Powder'
        Liquid = 'Liquid'
        Injection = 'Injection'
 
    class MorningTime(models.TextChoices):
        Before_Breakfast = 'BB'
        After_Breakfast = 'AB'

    class AfternoonTime(models.TextChoices):
        Before_Lunch = 'BL'
        After_Lunch = 'AL'

    class EveningTime(models.TextChoices):
        Before_Dinner = 'BD'
        After_Dinner = 'AD'
        Before_Sleep = 'BS'

    name = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    form = models.CharField(max_length=10, choices=MedicineForm.choices)
    is_in_morning = models.BooleanField(default=False)
    is_in_afternoon = models.BooleanField(default=False)
    is_in_evening = models.BooleanField(default=False)
    morning_time = models.CharField(max_length=2, choices=MorningTime.choices, blank=True)
    afternoon_time = models.CharField(max_length=2, choices=AfternoonTime.choices, blank=True)
    evening_time = models.CharField(max_length=2, choices=EveningTime.choices, blank=True)
    morning_quantity = models.CharField(max_length=5, blank=True)
    afternoon_quantity = models.CharField(max_length=5, blank=True)
    evening_quantity = models.CharField(max_length=5, blank=True)
    instructions = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class PrescriptionItem(models.Model):
    class MorningTime(models.TextChoices):
        Before_Breakfast = 'BB'
        After_Breakfast = 'AB'

    class AfternoonTime(models.TextChoices):
        Before_Lunch = 'BL'
        After_Lunch = 'AL'

    class EveningTime(models.TextChoices):
        Before_Dinner = 'BD'
        After_Dinner = 'AD'
        Before_Sleep = 'BS'

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription_number = models.IntegerField(default=1, null=True)
    name = models.CharField(max_length=100, blank=False)
    morning_time = models.CharField(max_length=2, choices=MorningTime.choices, blank=True)
    afternoon_time = models.CharField(max_length=2, choices=AfternoonTime.choices, blank=True)
    evening_time = models.CharField(max_length=2, choices=EveningTime.choices, blank=True)
    morning_quantity = models.CharField(max_length=5, blank=True)
    afternoon_quantity = models.CharField(max_length=5, blank=True)
    evening_quantity = models.CharField(max_length=5, blank=True)
    no_of_days = models.CharField(max_length=10, blank=True)
    instructions = models.CharField(max_length=100, blank=True)
    date_prescribed = models.DateField(auto_now_add=True)