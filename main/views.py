from appointment.models import Appointment
from main.models import Patient
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import date
from .forms import *

def loginuser(request): 
    if request.method == 'GET':
        return render(request, 'main/loginuser.html', {'login_form': AuthenticationForm() })
    else:
        #  Login user if allowed
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')


@login_required(login_url='loginuser')
def home(request):
    # pass number of patients
    patientcount = Patient.objects.count()

    # Pass today's appointments
    todaysapts = []
    today = date.today()
    todaydate = today.strftime("%Y-%m-%d")
    todayAptSet = Appointment.objects.filter(on_date = todaydate)
    todayaptscount = Appointment.objects.filter(on_date = todaydate).count()
    
    if request.method == 'GET':
        for apt in todayAptSet:
            todaysapts.append(apt)
        return render(request, 'main/home.html', {
            'appointments': todaysapts, 
            'selectedDateStr': '', 
            'todayaptscount': todayaptscount, 
            'patientcount': patientcount})

    elif 'aptsbydate' in request.POST:
        selectedDateStr = request.POST['datepicker']
        selectedDate = datetime.strptime(selectedDateStr, '%d-%m-%Y')
        aptsSet = Appointment.objects.filter(on_date = selectedDate)
        return render(request, 'main/home.html', {
            'appointments': aptsSet, 
            'selectedDateStr': selectedDateStr,
            'todayaptscount': todayaptscount, 
            'patientcount': patientcount })

def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('loginuser')

def searchpatient(request):
    query = request.GET['query']
    patientlistbyname = Patient.objects.filter(full_name__icontains=query)
    patientlistbynumber = Patient.objects.filter(
        case_paper_number__icontains=query)
    patientlist = patientlistbyname.union(patientlistbynumber)
    if patientlist.count() == 1:
        messages.add_message(request, messages.SUCCESS, str(patientlist.count()) + ' Patient Found!')
    elif patientlist.count() == 0:
        pass
    else:
        messages.add_message(request, messages.SUCCESS, str(patientlist.count()) + ' Patients Found!')
    return render(request, 'main/allpatients.html', {'patients': patientlist})

@login_required(login_url='loginuser')
def allpatients(request):
    if request.method == 'GET':
        patients = Patient.objects.order_by('id').reverse()
        return render(request, 'main/allpatients.html', {'patients': patients})

@login_required(login_url='loginuser')
def addpatient(request):
    form = AddPatientForm()
        # Get last case paper number and set next to case paper number input 
    last_number = None
    casepapernumber = 'ANC-1' 
    last_patient = Patient.objects.last()
    if last_patient:
        last_number = last_patient.case_paper_number
        hyphenindex = last_number.index('-')
        numberstring = last_number[hyphenindex + 1:]
        number = int(numberstring)
        casepapernumber = 'ANC-' + str(number + 1)

    if request.method == 'GET':
        return render(request, 'main/addpatient.html', {'casepapernumber': casepapernumber, 'form':form})
        
    elif request.method=='POST':
        form = AddPatientForm(request.POST) 
        try:
            if form.is_valid():
                newpatient = form.save(commit=False)
                if form.cleaned_data['category'] == 'ANC':
                    newpatient.is_anc = True
                if form.cleaned_data['category'] == 'INF':
                    newpatient.is_inf = True
                if form.cleaned_data['category'] == 'GYNAC':
                    newpatient.is_gynac = True
                newpatient.save() 
                patients = Patient.objects.order_by('id').reverse()
                messages.add_message(request, messages.SUCCESS, 'Patient Added Successfully!')
                return render(request, 'main/allpatients.html', {'patients': patients})
            else:
                return render (request, 'main/addpatient.html', {'casepapernumber': casepapernumber, 'form':form})
        except ValueError:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return render(request, 'main/addpatient.html', {'casepapernumber': casepapernumber, 'form':form})

@login_required(login_url='loginuser')        
def viewpatient(request, patient_pk):
    if request.method == 'GET':
        patient = get_object_or_404(Patient, pk=patient_pk)
        return render(request, 'main/viewpatient.html', {'patient': patient})

@login_required(login_url='loginuser')
def editpatient(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    if request.method == 'GET':
        editpatientform = EditPatientForm(instance=patient)
        return render(request, 'main/editpatient.html', {'patient': patient, 'form': editpatientform})
    elif request.method == 'POST':
        form = EditPatientForm(request.POST, instance=patient)
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Patient updated successfully!')
                return render(request, 'main/editpatient.html', {'patient': patient, 'form': form})
        except ValueError:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return render(request, 'main/editpatient.html', {'patient': patient, 'form':form})

@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def deletepatient(request, patient_pk):
    try:
        patient = get_object_or_404(Patient, pk=patient_pk)
        patient.delete()
        messages.add_message(request, messages.SUCCESS, 'Patient deleted successfully!')
        return redirect('allpatients')
    except:
        messages.add_message(request, messages.ERROR, 'Something went wrong! Try again later!')
        return redirect('allpatients')



def fetchpatientnames(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        patients = Patient.objects.filter(full_name__icontains=term)
        names = list()
        print(names)
        for patient in patients:
            names.append(patient.full_name)
        return JsonResponse(names, safe=False)

