from django.shortcuts import render
from main.models import Patient
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from datetime import date
from django.urls import reverse

# Create your views here.
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def addmedicine(request):
    form = AddMedicineForm()
    if request.method == 'GET':
        return render(request, 'medicine/addmedicine.html', {'form':form})
    elif request.method=='POST':
        form = AddMedicineForm(request.POST)   
        try:         
            if form.is_valid():
                newmed = form.save(commit=False)
                newmed.save()
                return redirect('allmedicines')
        except ValueError:
            messages.add_message(request, messages.ERROR, 'Please submit valid data')
            return render(request, 'medicine/addpatient.html', {'form':form})


#  All medicines list view
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def allmedicines(request):
    if request.method == 'GET':
        medicines = Medicine.objects.all()
        return render(request, 'medicine/allmedicines.html', {'medicines': medicines})

# edit medicine
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def editmedicine(request, medicine_pk):
    med = get_object_or_404(Medicine, pk=medicine_pk)
    if request.method == 'GET':
        editmedicineform = AddMedicineForm(instance=med)
        return render(request, 'medicine/editmedicine.html', {'medicine': med, 'form': editmedicineform})
    elif request.method == 'POST':
        form = AddMedicineForm(request.POST, instance=med)
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Medicine updated successfully!')
                return render(request, 'medicine/editmedicine.html', {'medicine': med, 'form': form})
        except:
            messages.add_message(request, messages.SUCCESS, 'Something went wrong!')
            return render(request, 'medicine/editmedicine.html')


@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def addprescription(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    form = PrescriptionItemForm()

    #  get previous prescription item for this patient
    previousprescriptionnumber = 1
    med = None
    previousprescriptiondate = None
    previousprescription = PrescriptionItem.objects.all().filter(patient=patient).last()

    # get today's all prescription items
    today = date.today() 
    todayday = today.day
    todaymonth = today.month
    todayyear = today.year
    previoustodaysprescriptions = []
    todaysprescriptions = PrescriptionItem.objects.all().filter(patient=patient, date_prescribed=date(todayyear, todaymonth, todayday))
    if todaysprescriptions:
        for todaysprescription in todaysprescriptions:
            previoustodaysprescriptions.append(todaysprescription)

    if previousprescription:
        previousprescriptiondate = previousprescription.date_prescribed
        previousprescriptionnumber = previousprescription.prescription_number
    if request.method == 'GET':
        return render(request, 'medicine/addprescription.html', {'form':form, 'patient':patient, 'prescriptions': previoustodaysprescriptions})
    if 'getmedbyname' in request.POST:
        med = get_object_or_404(Medicine, name=request.POST['medname'])
        form = PrescriptionItemForm(instance=med)
        return render(request, 'medicine/addprescription.html', {'form': form, 'patient':patient, 'medicine': med, 'prescriptions': previoustodaysprescriptions})
    if 'addprescription' in request.POST:
        form = PrescriptionItemForm(request.POST)  
        if form.is_valid():
            try:
                pitem = form.save(commit=False)
                if previousprescriptiondate:
                    if previousprescriptiondate.strftime("%Y-%m-%d") == date.today().strftime("%Y-%m-%d"):
                        pitem.prescription_number = previousprescriptionnumber
                    else:
                        pitem.prescription_number = previousprescriptionnumber + 1
                else:
                    pitem.prescription_number = 1            
                pitem.patient = patient
                pitem.save()
                return redirect(reverse('addprescription', kwargs={"patient_pk": patient_pk}))
            except ValueError as v:
                print(v)
        return render(request, 'medicine/addprescription.html', {'form':PrescriptionItemForm(), 'patient': patient, 'prescriptions': previoustodaysprescriptions})


@login_required(login_url='loginuser')
def allprescriptions(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    listoflistofp = []
    listofdates = []
    lastprescription = PrescriptionItem.objects.all().filter(patient=patient).last()
    if lastprescription:
        lastprescriptionnumber = lastprescription.prescription_number
        i = 1
        while i <= lastprescriptionnumber:
            allponsamedate = PrescriptionItem.objects.all().filter(patient=patient,prescription_number=i)
            allponsamedatelist = []
            for p in allponsamedate:
                allponsamedatelist.append(p)
            listoflistofp.append(allponsamedatelist)
            listofdates.append(allponsamedatelist[0].date_prescribed)
            i += 1         
    if request.method == 'GET':
        return render(request, 'medicine/allprescriptions.html', {'patient': patient, 'listoflistofp': listoflistofp, 'dates': listofdates})


# for autocomplete feature in add prescription form
def fetchmednames(request):
    if 'term' in request.GET:
        medicines = Medicine.objects.filter(name__icontains=request.GET.get('term'))
        names = list()
        for med in medicines:
            names.append(med.name)
        return JsonResponse(names, safe=False)