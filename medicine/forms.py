from django.forms import ModelForm, widgets
from medicine.models import Medicine, PrescriptionItem

class AddMedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'name', 
            'brand', 
            'form', 
            'is_in_morning', 
            'is_in_afternoon', 
            'is_in_evening', 
            'morning_time', 
            'afternoon_time', 
            'evening_time', 
            'morning_quantity', 
            'afternoon_quantity', 
            'evening_quantity',
            'instructions',
        ]
        labels = {
            'is_in_morning': 'Morning',
            'is_in_afternoon': 'Afternoon',
            'is_in_evening': 'Evening',
        }

class PrescriptionItemForm(ModelForm):
    class Meta:
        model = PrescriptionItem
        fields = "__all__"
        exclude = ['patient', 'prescription_number', 'date_prescribed']
        labels = {
            'name': 'Medicine',
            'no_of_days': 'Days',
            'morning_quantity': 'Morning',
            'afternoon_quantity': 'Afternoon',
            'evening_quantity': 'Evening',
            'morning_time': '',
            'afternoon_time': '',
            'evening_time': '',
        }
        widgets = {
            'date_prescribed': widgets.DateInput(attrs={'class':'form-control', 'type':'date'}),
         }
