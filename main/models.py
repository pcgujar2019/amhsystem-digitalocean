from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.
class PatientCategory(models.TextChoices):
    ANC = 'ANC'
    INF = 'INF'
    GYNAC = 'GYNAC'
class PatientGender(models.TextChoices):
    MALE = 'Male' 
    FEMALE = 'Female'
class Patient(models.Model):
    category = models.CharField(max_length=5, choices=PatientCategory.choices, default=PatientCategory.ANC)
    case_paper_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    age = models.IntegerField(blank=False, validators=[MinValueValidator(12), MaxValueValidator(65)])
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=PatientGender.choices, default=PatientGender.FEMALE)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    address_line_1 = models.CharField(max_length=100, blank=True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=False)
    pin_code = models.IntegerField(blank=True, null=True)
    referred_by = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_inf = models.BooleanField(default=False)
    is_anc = models.BooleanField(default=False)
    is_gynac = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name