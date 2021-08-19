from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db.models.fields import CharField
from main.models import Patient

# Create your models here.
class FertilitySheet(models.Model):
    class CycleValue(models.TextChoices):
        _21_To_25 = '21-25'
        _28_To_35 = '28-35'
        _45_To_60 = '45-60'
        _60_To_90 = '60-90'
        _90_To_120 = '90-120'
        Beyond_120 = 'Beyond 120'
        Need_Rx = 'Need Rx'
    
    class MC(models.TextChoices):
        regular = 'Regular'
        irregular = 'Irregular'
    class MedicationNeeded(models.TextChoices):
        yes = 'Yes'
        no = 'No'

    height = models.CharField(max_length=10, blank=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    bmi = models.CharField(max_length=10, blank=True, null=True)
    trying_for_years = models.CharField(max_length=10, blank=True, null=True)
    trying_for_months = models.CharField(max_length=10, blank=True, null=True)
    menstrual_cycle = models.CharField(max_length=20, choices=MC.choices, default=MC.regular)
    bleeding_days = models.CharField(max_length=10, blank=True, null=True)
    lmp = models.DateField(blank=True, null=True)
    cycle = models.CharField(max_length=20, choices=CycleValue.choices, default=CycleValue._21_To_25)
    medication_needed_for_period = models.CharField(max_length=20, choices=MedicationNeeded.choices, default=MedicationNeeded.no)
    mother_menopause_age = models.FloatField(blank=True, null=True)

    intercourse_per_week = models.IntegerField(default=0)
    intercourse_comment = models.CharField(max_length=150, blank=True)
    is_had_surgery = models.BooleanField(default=False)
    surgery_comment = models.CharField(max_length=200,blank=True)
    is_recent_weight_gain_or_loss = models.BooleanField(default=False)
    is_hair_loss = models.BooleanField(default=False)
    is_asthma = models.BooleanField(default=False)
    is_hepatitis = models.BooleanField(default=False)
    is_anorexia_bulimia = models.BooleanField(default=False)
    is_lumps = models.BooleanField(default=False)
    is_seizures_epilepsy = models.BooleanField(default=False)
    is_vaginal_infections = models.BooleanField(default=False)
    is_diabetes = models.BooleanField(default=False)
    is_tuberculosis = models.BooleanField(default=False)
    is_migraine_headaches = models.BooleanField(default=False)
    is_high_bp = models.BooleanField(default=False)
    is_mother_diabetic = models.BooleanField(default=False)
    is_father_diabetic = models.BooleanField(default=False)
    is_mother_htn = models.BooleanField(default=False)
    is_father_htn = models.BooleanField(default=False)
    physical_symptoms_comment = models.CharField(max_length=150, blank=True)

    laparoscopy_findings = models.TextField(blank=True)
    hsg_findings = models.TextField(blank=True)
    ll_no_of_cycles_1 = models.CharField(max_length=10, blank=True)
    ll_tic_1 = models.CharField(max_length=10, blank=True)
    ll_iui_1 = models.CharField(max_length=10, blank=True)
    ll_pregnant_1 = models.BooleanField(default=False)
    ll_comment_1 = models.CharField(max_length=100, blank=True)
    ll_no_of_cycles_2 = models.CharField(max_length=10, blank=True)
    ll_tic_2 = models.CharField(max_length=10, blank=True)
    ll_iui_2 = models.CharField(max_length=10, blank=True)
    ll_pregnant_2 = models.BooleanField(default=False)
    ll_comment_2 = models.CharField(max_length=100, blank=True)
    ll_no_of_cycles_3 = models.CharField(max_length=10, blank=True)
    ll_tic_3 = models.CharField(max_length=10, blank=True)
    ll_iui_3 = models.CharField(max_length=10, blank=True)
    ll_pregnant_3 = models.BooleanField(default=False)
    ll_comment_3 = models.CharField(max_length=100, blank=True)
    ll_no_of_cycles_4 = models.CharField(max_length=10, blank=True)
    ll_tic_4 = models.CharField(max_length=10, blank=True)
    ll_iui_4 = models.CharField(max_length=10, blank=True)
    ll_pregnant_4 = models.BooleanField(default=False)
    ll_comment_4 = models.CharField(max_length=100, blank=True)
    ivf_comment_I = models.TextField(blank=True)
    ivf_comment_II = models.TextField(blank=True)


    date_added = models.DateTimeField(auto_now_add=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True)

class MaleMedicalHistory(models.Model):
    husband_name = models.CharField(blank=True, max_length=50)
    husband_age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(15), MaxValueValidator(60)])
    husband_work = models.CharField(blank=True, max_length=20)
    sperm_count_I = models.FloatField(default=0)
    sperm_count_II = models.FloatField(default=0)
    sperm_count_III = models.FloatField(default=0)
    sperm_motility_I = models.FloatField(default=0)
    sperm_motility_II = models.FloatField(default=0)
    sperm_motility_III = models.FloatField(default=0)
    surgical_dm_htn_comment = models.CharField(blank=True, max_length=200)
    usg_of_scrotum_comment = models.CharField(blank=True, max_length=200)
    fhs_report = models.CharField(max_length=100, blank=True)
    lh_report = models.CharField(max_length=100, blank=True)
    testosterone_report = models.CharField(max_length=100, blank=True)
    hiv_report = models.CharField(max_length=100, blank=True)
    medical_history = models.TextField(blank=True)
    current_rx_husband = models.TextField(blank=True)
    current_rx_wife = models.TextField(blank=True)
    allergic_to = models.TextField(blank=True)
    past_treatment_at_our_clinic = models.TextField(blank=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class WifeExamination(models.Model):
    amh = models.CharField(max_length=25, blank=True)
    fsh = models.CharField(max_length=25, blank=True)
    lh = models.CharField(max_length=25, blank=True)
    prolactin = models.CharField(max_length=25, blank=True)
    andro = models.CharField(max_length=25, blank=True)
    testo = models.CharField(max_length=25, blank=True)
    tsh = models.CharField(max_length=25, blank=True)
    hb = models.CharField(max_length=25, blank=True)
    sugar = models.CharField(max_length=25, blank=True)
    hba1c = models.CharField(max_length=25, blank=True)
    hiv = models.CharField(max_length=25, blank=True)
    hbsag = models.CharField(max_length=25, blank=True)
    vdrl = models.CharField(max_length=25, blank=True)
    urea = models.CharField(max_length=25, blank=True)
    creat = models.CharField(max_length=25, blank=True)
    lipid_profile = models.CharField(max_length=25, blank=True)
    ac_antibodies = models.CharField(max_length=25, blank=True)
    anti_dsdna = models.CharField(max_length=25, blank=True)
    bg_antibodies = models.CharField(max_length=25, blank=True)
    lupus_anticoagulant = models.CharField(max_length=25, blank=True)
    protein_c = models.CharField(max_length=25, blank=True)
    protein_s = models.CharField(max_length=25, blank=True)
    karyotp = models.CharField(max_length=25, blank=True)
    other = models.CharField(max_length=100, blank=True)
    usg = models.CharField(max_length=100, blank=True)
    lmp = models.DateField(blank=True, null=True)
    day = models.CharField(max_length=100, blank=True)
    plan = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True)

class Investigation(models.Model):
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    hb_on_date1 = models.FloatField(blank=True, null=True)
    hb_on_date2 = models.FloatField(blank=True, null=True)
    hb_on_date3 = models.FloatField(blank=True, null=True)
    bloodGroup = models.CharField(max_length=15, blank=True)
    bslr_on_date1 = models.CharField(max_length=10, blank=True)
    bslr_on_date2 = models.CharField(max_length=10, blank=True)
    bslr_on_date3 = models.CharField(max_length=10, blank=True)
    gct_on_date1 = models.CharField(max_length=10, blank=True)
    gct_on_date2 = models.CharField(max_length=10, blank=True)
    gct_on_date3 = models.CharField(max_length=10, blank=True)
    aust_antg_on_date1 = models.CharField(max_length=10, blank=True)
    aust_antg_on_date2 = models.CharField(max_length=10, blank=True)
    aust_antg_on_date3 = models.CharField(max_length=10, blank=True)
    elisa_on_date1 = models.CharField(max_length=10, blank=True)
    elisa_on_date2 = models.CharField(max_length=10, blank=True)
    elisa_on_date3 = models.CharField(max_length=10, blank=True)
    tsh_on_date1 = models.CharField(max_length=10, blank=True)
    tsh_on_date2 = models.CharField(max_length=10, blank=True)
    tsh_on_date3 = models.CharField(max_length=10, blank=True)
    urine_on_date1 = models.CharField(max_length=10, blank=True)
    urine_on_date2 = models.CharField(max_length=10, blank=True)
    urine_on_date3 = models.CharField(max_length=10, blank=True)
    empty11 = models.CharField(max_length=20, blank=True)
    empty12 = models.CharField(max_length=20, blank=True)
    empty13 = models.CharField(max_length=20, blank=True)
    empty14 = models.CharField(max_length=20, blank=True)
    empty21 = models.CharField(max_length=20, blank=True)
    empty22 = models.CharField(max_length=20, blank=True)
    empty23 = models.CharField(max_length=20, blank=True)
    empty24 = models.CharField(max_length=20, blank=True)
    empty31 = models.CharField(max_length=20, blank=True)
    empty32 = models.CharField(max_length=20, blank=True)
    empty33 = models.CharField(max_length=20, blank=True)
    empty34 = models.CharField(max_length=20, blank=True)
    empty41 = models.CharField(max_length=20, blank=True)
    empty42 = models.CharField(max_length=20, blank=True)
    empty43 = models.CharField(max_length=20, blank=True)
    empty44 = models.CharField(max_length=20, blank=True)
    instructions = models.TextField(blank=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    

class TtDose(models.Model):
    tt1_date = models.DateField(blank=True, null=True)
    tt2_date = models.DateField(blank=True, null=True)
    instructions = models.TextField(blank=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)


    # USG 
class Usg(models.Model):
    r1_check = models.BooleanField(default=False)
    r2_check = models.BooleanField(default=False)
    r3_check = models.BooleanField(default=False)
    r4_check = models.BooleanField(default=False)
    r5_check = models.BooleanField(default=False)
    r6_check = models.BooleanField(default=False)
    r7_check = models.BooleanField(default=False)
    r8_check = models.BooleanField(default=False)
    r9_check = models.BooleanField(default=False)
    r1_comment = models.CharField(max_length=50, blank=True)
    r2_comment = models.CharField(max_length=50, blank=True)
    r3_comment = models.CharField(max_length=50, blank=True)
    r4_comment = models.CharField(max_length=50, blank=True)
    r5_comment = models.CharField(max_length=50, blank=True)
    r6_comment = models.CharField(max_length=50, blank=True)
    r7_comment = models.CharField(max_length=50, blank=True)
    r8_comment = models.CharField(max_length=50, blank=True)
    r9_comment = models.CharField(max_length=50, blank=True)
    instructions = models.TextField(blank=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)












class Gender(models.TextChoices):
    MALE = 'Male' 
    FEMALE = 'Female'
class AncOpdFirstBlock(models.Model):
    class GOptions(models.TextChoices):
        PTND = 'PTND'
        FTND = 'FTND'
        LSCS = 'LSCS'
        IUD = 'IUD'
        Missed_Abortion = 'Missed Abortion'
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True)
    married_since = models.CharField(max_length=10, blank=True)
    visit_no = models.IntegerField(default=0, blank=True, null=True)
    consanguinity = models.BooleanField(default=False)
    g1 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g2 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g3 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g4 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g5 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)

    g1_age = models.CharField(max_length=10, blank=True)
    g2_age = models.CharField(max_length=10, blank=True)
    g3_age = models.CharField(max_length=10, blank=True)
    g4_age = models.CharField(max_length=10, blank=True)
    g5_age = models.CharField(max_length=10, blank=True)
    g1_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g2_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g3_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g4_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g5_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g1_comment = models.CharField(max_length=100, blank=True)
    g2_comment = models.CharField(max_length=100, blank=True)
    g3_comment = models.CharField(max_length=100, blank=True)
    g4_comment = models.CharField(max_length=100, blank=True)
    g5_comment = models.CharField(max_length=100, blank=True)

    present_pregnancy = CharField(max_length=20, blank=True)
    flu_date = models.DateField(blank=True, null=True)
    lmp = models.DateField(blank=True, null=True)
    date_added = models.DateField(blank=False)


class AncOpdBlock(models.Model):
    visit_no = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True)
    advised = models.CharField(max_length=100, blank=True)
    gest_period = models.CharField(max_length=20, blank=True)
    co = models.CharField(max_length=100, blank=True)
    bp = models.CharField(max_length=20, blank=True)
    flu_date = models.DateField(blank=True, null=True)
    scan_so_date = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True)
    afi = models.FloatField(null=True, blank=True)
    efw = models.FloatField(null=True, blank=True)
    doppler = models.CharField(max_length=100, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date_added = models.DateField(blank=False)













class GynacOpdFirstBlock(models.Model):
    class GOptions(models.TextChoices):
        PTND = 'PTND'
        FTND = 'FTND'
        LSCS = 'LSCS'
        IUD = 'IUD'
        Missed_Abortion = 'Missed Abortion'
    visit_no = models.IntegerField(default=0, blank=True, null=True)
    is_married = models.BooleanField(default=False)
    married_since = models.CharField(max_length=10, blank=True)
    g1 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g2 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g3 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g4 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)
    g5 = models.CharField(max_length=20, choices=GOptions.choices, blank=True)

    g1_age = models.CharField(max_length=10, blank=True)
    g2_age = models.CharField(max_length=10, blank=True)
    g3_age = models.CharField(max_length=10, blank=True)
    g4_age = models.CharField(max_length=10, blank=True)
    g5_age = models.CharField(max_length=10, blank=True)
    g1_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g2_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g3_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g4_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g5_sex = models.CharField(max_length=10, choices=Gender.choices, blank=True)
    g1_comment = models.CharField(max_length=100, blank=True)
    g2_comment = models.CharField(max_length=100, blank=True)
    g3_comment = models.CharField(max_length=100, blank=True)
    g4_comment = models.CharField(max_length=100, blank=True)
    g5_comment = models.CharField(max_length=100, blank=True)

    is_family_completed = models.BooleanField(default=False)
    is_tl_done = models.BooleanField(default=False)

    flu_date = models.DateField(blank=True, null=True)

    date_added = models.DateField(blank=False)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True)


class GynacOpdBlock(models.Model):
    date_added = models.DateField(blank=False)
    visit_no = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True)
    advised = models.CharField(max_length=100, blank=True)
    lmp = models.DateField(blank=True, null=True)
    co = models.CharField(max_length=100, blank=True)
    bp = models.CharField(max_length=20, blank=True)
    flu_date = models.DateField(blank=True, null=True)
    
    scan_date = models.DateField(blank=True, null=True)
    scan_description = models.TextField(blank=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

 















# INF paper
class InfPlanOneFirstBlock(models.Model):
    date_added = models.DateField(blank=False)
    lmp = models.DateField(blank=True, null=True)
    days = models.CharField(max_length=15, blank=True)
    visit_no = models.IntegerField(default=0, blank=True, null=True)

    tablet_name = models.CharField(max_length=150, blank=True)
    tablet_qty = models.CharField(max_length=10, blank=True)
    morning_qty = models.CharField(max_length=10, blank=True)
    afternoon_qty = models.CharField(max_length=10, blank=True)
    evening_qty = models.CharField(max_length=10, blank=True)
    flu_date = models.DateField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

class InfPlanOneBlock(models.Model):
    date_added = models.DateField(blank=False)
    visit_no = models.IntegerField(blank=True, null=True)
    right = models.CharField(max_length=10, blank=True)
    left = models.CharField(max_length=10, blank=True)
    et = models.CharField(max_length=10, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    flu_date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)









class InfPlanTwoFirstBlock(models.Model):
    date_added = models.DateField(blank=False)
    lmp = models.DateField(blank=True, null=True)
    days = models.CharField(max_length=15, blank=True)
    visit_no = models.IntegerField(default=0, blank=True, null=True)

    tablet_name = models.CharField(max_length=150, blank=True)
    tablet_qty = models.CharField(max_length=10, blank=True)
    tab_morning_qty = models.CharField(max_length=10, blank=True)
    tab_afternoon_qty = models.CharField(max_length=10, blank=True)
    tab_evening_qty = models.CharField(max_length=10, blank=True)

    injection_name = models.CharField(max_length=150, blank=True)
    injection_qty = models.CharField(max_length=10, blank=True)
    day1 = models.CharField(max_length=50, blank=True)
    day2 = models.CharField(max_length=50, blank=True)
    day3 = models.CharField(max_length=50, blank=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)

    flu_date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)





class InfPlanTwoBlock(models.Model):
    date_added = models.DateField(blank=False)
    visit_no = models.IntegerField(blank=True, null=True)
    right = models.CharField(max_length=10, blank=True)
    left = models.CharField(max_length=10, blank=True)
    et = models.CharField(max_length=10, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    flu_date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
