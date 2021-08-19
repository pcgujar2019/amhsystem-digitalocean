from django.forms import ModelForm, widgets
from .models import Patient

class AddPatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
            'category', 
            'case_paper_number', 
            'full_name', 
            'age', 
            'birth_date', 
            'gender', 
            'mobile_number', 
            'email', 
            'address_line_1', 
            'address_line_2', 
            'city', 
            'pin_code', 
            'referred_by',
        ]
        widgets = {
            # 'birth_date': widgets.Input(attrs={'autocomplete':'off'}),
            'birth_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'mobile_number': widgets.NumberInput(attrs={'type': 'number'}),
            'email': widgets.EmailInput(),
            'pin_code': widgets.NumberInput(attrs={'required': 'required'}),
         }

class EditPatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
            'case_paper_number', 
            'full_name', 
            'age', 
            'birth_date', 
            'gender', 
            'mobile_number', 
            'email', 
            'address_line_1', 
            'address_line_2', 
            'city', 
            'pin_code', 
            'referred_by',
            'is_anc',
            'is_inf',
            'is_gynac'
        ]
        widgets = {
            # 'birth_date': widgets.Input(attrs={'autocomplete':'off'}),
            'birth_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'mobile_number': widgets.NumberInput(attrs={'type': 'number'}),
            'email': widgets.EmailInput(),
            'pin_code': widgets.NumberInput(attrs={'required': 'required'}),
         }
