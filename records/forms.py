from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import *

class FertilitySheetForm(ModelForm):
    class Meta:
        model = FertilitySheet
        fields = "__all__"
        exclude = ['date_added', 'patient']
        labels = {
            'height': 'Height(cm)',
            'weight': 'Weight(Kg)',
            'bmi': 'BMI',
            'trying_for_years': 'Years',
            'trying_for_months': 'Months',
            'menstrual_cycle': 'Menstrual Cycle',
            'bleeding_days': 'How many days bleeding do you have?',
            'lmp': 'LMP',
            'intercourse_comment': 'Comment',
            'medication_needed_for_period': 'Do you need medication for period?',
            'mother_menopause_age': 'Age of Menopause in Mother',
            'surgery_comment': 'Have you had any surgeries?',
            'is_recent_weight_gain_or_loss': 'Recent Weight gain/loss',
            'is_hair_loss': 'Hair Loss',
            'is_asthma': 'Asthma',
            'is_hepatitis': 'Hepatitis',
            'is_anorexia_bulimia': 'Anorexia/Bulimia',
            'is_lumps': 'Lumps',
            'is_seizures_epilepsy': 'Seizures/Epilepsy',
            'is_vaginal_infections': 'Vaginal Infections',
            'is_diabetes': 'Vaginal Infections',
            'is_tuberculosis': 'Tuberculosis',
            'is_migraine_headaches': 'Migraine/Headaches',
            'is_high_bp': 'High B.P',
            'physical_symptoms_comment': 'Other (If any)',
            'is_mother_diabetic': '',
            'is_father_diabetic': '',
            'is_mother_htn': '',
            'is_father_htn': '',
            'll_no_of_cycles_1': '',
            'll_no_of_cycles_2': '',
            'll_no_of_cycles_3': '',
            'll_no_of_cycles_4': '',
            'll_tic_1': '',
            'll_tic_2': '',
            'll_tic_3': '',
            'll_tic_4': '',
            'll_iui_1': '',
            'll_iui_2': '',
            'll_iui_3': '',
            'll_iui_4': '',
            'll_pregnant_1': '',
            'll_pregnant_2': '',
            'll_pregnant_3': '',
            'll_pregnant_4': '',
            'll_comment_1': '',
            'll_comment_2': '',
            'll_comment_3': '',
            'll_comment_4': '',
            'ivf_comment_I': 'IVF(I)',
            'ivf_comment_II': 'IVF(II)',
        }
        widgets = {
            'lmp': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'POST'

class MaleMedicalHistoryForm(ModelForm):
    class Meta:
        model = MaleMedicalHistory
        fields = "__all__"
        exclude = ['date_added', 'patient']
        labels = {
            'sperm_count_I': '',
            'sperm_count_II': '',
            'sperm_count_III': '',
            'sperm_motility_I': '',
            'sperm_motility_II': '',
            'sperm_motility_III': '',
            'surgical_dm_htn_comment': 'Surgical/DM/HTN',
            'usg_of_scrotum_comment': 'USG of Scrotum',
            'fhs_report': 'FHS',
            'lh_report': 'LH',
            'testosterone_report': 'Testo.',
            'hiv_report': 'HIV',
            'current_rx_husband': 'Husband',
            'current_rx_wife': 'Wife',
            'allergic_to': 'Allergic To any medications',
            'past_treatment_at_our_clinic': 'Past Treatment at our clinic',
        }

class WifeExaminationForm(ModelForm):
    class Meta:
        model = WifeExamination
        fields = "__all__"
        exclude = ['date_added', 'patient']
        labels = {
            'amh': 'AMH',
            'fsh': 'FSH',
            'lh': 'LH',
            'prolactin': 'PROLACTIN',
            'andro': 'ANDRO.',
            'testo': 'TESTO.',
            'tsh': 'TSH',
            'hb': 'Hb.',
            'sugar': 'SUGAR(R/F/PP)',
            'hba1c': 'HbA1C',
            'hiv': 'HIV',
            'hbsag': 'HBsAg',
            'vdrl': 'VDRL',
            'urea': 'UREA',
            'creat': 'CREAT.',
            'lipid_profile': 'Lipid Profile',
            'ac_antibodies': 'Anti-Cardiolipin antibodies (IgG/IgM)',
            'anti_dsdna': 'Anti DSDNA',
            'bg_antibodies': 'B2 Glycoprotein antibodies (IgG/IgM)',
            'lupus_anticoagulant': 'Lupus Anticoagulant',
            'protein_c': 'Protein C',
            'protein_s': 'Protein S',
            'karyotp': 'Karyotping of (H/W/POC)',
            'other': 'Other',
            'usg': 'USG',
            'lmp': 'LMP',
            'day': 'DAY',
            'plan': '',
        }
        widgets = {
            'lmp': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'day': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }

class InvestigationForm(ModelForm):
    class Meta:
        model = Investigation
        fields = "__all__"
        exclude = ['patient']
        labels = {
            'date1': '',
            'date2': '',
            'date3': '',
            'hb_on_date1': '',
            'hb_on_date2': '',
            'hb_on_date3': '',
            'bloodGroup': '',
            'bslr_on_date1': '',
            'bslr_on_date2': '',
            'bslr_on_date3': '',
            'gct_on_date1': '',
            'gct_on_date2': '',
            'gct_on_date3': '',
            'aust_antg_on_date1': '',
            'aust_antg_on_date2': '',
            'aust_antg_on_date3': '',
            'elisa_on_date1': '',
            'elisa_on_date2': '',
            'elisa_on_date3': '',
            'tsh_on_date1': '',
            'tsh_on_date2': '',
            'tsh_on_date3': '',
            'urine_on_date1': '',
            'urine_on_date2': '',
            'urine_on_date3': '',

            'empty11': '',
            'empty12': '',
            'empty13': '',
            'empty14': '',
            'empty21': '',
            'empty22': '',
            'empty23': '',
            'empty24': '',
            'empty31': '',
            'empty32': '',
            'empty33': '',
            'empty34': '',
            'empty41': '',
            'empty42': '',
            'empty43': '',
            'empty44': '',
            'instructions': 'Instructions IF ANY'

        }
        widgets = {
            'date1': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'date2': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'date3': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),

         }

class TtDoseForm(ModelForm):
    class Meta:
        model = TtDose
        fields = "__all__"
        exclude = ['patient']
        labels = {
            'tt1_date': '',
            'tt2_date': '',
            'instructions': 'Instructions IF ANY'
        }
        widgets = {
            'tt1_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'tt2_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }

class UsgForm(ModelForm):
    class Meta:
        model = Usg
        fields = "__all__"
        exclude = ['patient']
        labels = {
            'r1_check': '',          
            'r2_check': '',          
            'r3_check': '',          
            'r4_check': '',          
            'r5_check': '',          
            'r6_check': '',          
            'r7_check': '',          
            'r8_check': '',          
            'r9_check': '', 
            'r1_comment': '',          
            'r2_comment': '',          
            'r3_comment': '',          
            'r4_comment': '',          
            'r5_comment': '',          
            'r6_comment': '',          
            'r7_comment': '',          
            'r8_comment': '',          
            'r9_comment': '', 
            'instructions': 'Instructions IF ANY'
        }























class AncOpdFirstBlockForm(ModelForm):
    class Meta:
        model = AncOpdFirstBlock
        fields = "__all__"
        exclude = ['patient']
        labels = {
            'date_added': 'Date',
            'married_since': 'Married Since',
            'visit_no': 'Visit No.',
            'consanguinity': 'Consanguinity',
            'g1': '',
            'g2': '',
            'g3': '',
            'g4': '',
            'g5': '',
            'g1_age': '',
            'g2_age': '',
            'g3_age': '',
            'g4_age': '',
            'g5_age': '',
            'g1_sex': '',
            'g2_sex': '',
            'g3_sex': '',
            'g4_sex': '',
            'g5_sex': '',
            'g1_comment': '',
            'g2_comment': '',
            'g3_comment': '',
            'g4_comment': '',
            'g5_comment': '',
            'present_pregnancy': 'Present Pregnancy',
            'lmp': 'LMP',  
            'flu_date': 'FLU'         
        }
        widgets = {
            'lmp': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date_a': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'date_added_a': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }


class AncOpdBlockForm(ModelForm):
    class Meta:
        model = AncOpdBlock
        fields = "__all__"
        exclude = ['patient']
        labels = {
            'date_added': 'Date',
            'visit_no': 'Visit No.',
            'weight': 'Weight',
            'advised': 'Advised',
            'gest_period': 'Gest period',
            'co': 'c/o',
            'bp': 'BP',
            'flu_date': 'FLU',
            'scan_so_date': 'Scan s/o',
            'comment': 'Comment',
            'afi': 'AFI(cm)',
            'efw': 'EFW(Kg)',           
            'doppler': 'Doppler',      
        }
        widgets = {
            'date_added': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'scan_so_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }

class GynacOpdFirstBlockForm(ModelForm):
    class Meta:
        model = GynacOpdFirstBlock
        fields = "__all__"
        exclude = ['patient']
        labels = {
            'date_added': 'Date',
            'married_since': 'Married since',
            'visit_no': '',
            'is_married': 'Married',
            'g1': '',
            'g2': '',
            'g3': '',
            'g4': '',
            'g5': '',
            'g1_age': '',
            'g2_age': '',
            'g3_age': '',
            'g4_age': '',
            'g5_age': '',
            'g1_sex': '',
            'g2_sex': '',
            'g3_sex': '',
            'g4_sex': '',
            'g5_sex': '',
            'g1_comment': '',
            'g2_comment': '',
            'g3_comment': '',
            'g4_comment': '',
            'g5_comment': '',
            'is_family_completed': '',
            'is_tl_done': '',  
            'flu_date': ''         
        }
        widgets = {
            'date_added': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }

class GynacOpdBlockForm(ModelForm):
    class Meta:
        model = GynacOpdBlock
        fields = "__all__"
        exclude = ['patient']
        widgets = {
            'date_added': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'lmp': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'scan_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
         }
        labels = {
            'date_added': '',
            'visit_no': '',
            'weight': '',
            'advised': '',
            'lmp': '',
            'co': '',
            'bp': '',
            'flu_date': '',
            'scan_date': '',
            'scan_description': ''
        }

class InfPlanOneFirstBlockForm(ModelForm):
    class Meta:
        model = InfPlanOneFirstBlock
        fields = "__all__"
        exclude = ['patient']
        widgets = {
            'date_added': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'lmp': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
        }
        labels = {
            'date_added': 'Date',
            'visit_no': 'Visit No.',
            'lmp': 'LMP', 
            'days': 'Days', 
            'tablet_name': 'Tab', 
            'tablet_qty': 'Qty',
            'morning_qty': 'Morning', 
            'afternoon_qty': 'Afternoon', 
            'evening_qty': 'Evening', 
            'flu_date': 'FLU', 
        }

class InfPlanOneBlockForm(ModelForm):
    class Meta:
        model = InfPlanOneBlock
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date_added': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
        }
        labels = {
            'date_added': 'Date',
            'visit_no': 'Visit No',
            'right': 'Right',
            'left': 'Left',
            'et': 'Et',
            'comment': 'Description',
            'flu_date': 'FLU',
        }

class InfPlanTwoFirstBlockForm(ModelForm):
    class Meta:
        model = InfPlanTwoFirstBlock
        fields = "__all__"
        exclude = ['patient']
        widgets = {
            'date_added': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'lmp': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'date1': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'date2': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'date3': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
        }
        labels = {
            'date_added': 'Date',
            'visit_no': 'Visit No',
            'lmp': 'LMP', 
            'days': 'Days', 
            'tablet_name': 'Tab', 
            'tablet_qty': 'Qty',
            'injection_name': 'Injection',
            'injection_qty': 'Qty',
            'day1': '',
            'day2': '',
            'day3': '',
            'date1': '',
            'date2': '',
            'date3': '',
            'tab_morning_qty': 'Morning', 
            'tab_afternoon_qty': 'Afternoon', 
            'tab_evening_qty': 'Evening', 
            'flu_date': 'FLU', 
        }

class InfPlanTwoBlockForm(ModelForm):
    class Meta:
        model = InfPlanTwoBlock
        fields = '__all__'
        exclude = ['patient']
        widgets = {
            'date_added': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'flu_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
        }
        labels = {
            'date_added': 'Date',
            'visit_no': 'Visit No',
            'right': 'Right',
            'left': 'Left',
            'et': 'Et',
            'comment': 'Description',
            'flu_date': 'FLU',
        }