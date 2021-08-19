from django.forms import ModelForm, widgets
from .models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        

        fields = '__all__'
        exclude = ['date_added', 'patient', 'visit_no']

        widgets = {
            'on_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }

        labels = {
            'on_date': 'Date of Appointment',
            'reason': 'Reason',
            'patient_name': 'Appointment For',
        }