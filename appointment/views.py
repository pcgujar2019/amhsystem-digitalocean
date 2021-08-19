from .models import Appointment
from main.models import Patient
from .forms import AppointmentForm
from django.http import JsonResponse
from datetime import datetime
from django.contrib import messages

from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def addappointment(request):
    form = AppointmentForm()
    if 'getpatientbyname' in request.POST:
        patientname = request.POST['patientname']
        patient = Patient.objects.get(full_name=patientname)
        form = AppointmentForm()
        return render(request, 'appointment/addappointment.html', {'form': form, 'patientname':patient.full_name, })


    if 'addappointment' in request.POST:
        patientname = request.POST['patient_name']
        on_date = request.POST['on_date']
        patient = Patient.objects.get(full_name=patientname)
        date = datetime.strptime(on_date, "%d-%m-%Y").strftime('%Y-%m-%d')
        isAptExist = Appointment.objects.filter(on_date=date, patient=patient)
        if isAptExist:
            messages.error(request, 'Duplicate Appointment! Apt for this patient on ' + on_date + ' is already added!')
            return render(request, 'appointment/addappointment.html', {'form': form, 'patientname':patient.full_name,})
        else:
            try:
                form = AppointmentForm(request.POST)
                addform = form.save(commit=False)
                addform.patient = patient
                messages.add_message(request, messages.SUCCESS, 'Appointment Added Successfully!!')
                addform.save()
            except:
                messages.error(request, 'Something went wrong!')
        return render(request, 'appointment/addappointment.html', {'form': form, 'patientname':patient.full_name,})

    
    if request.method == 'GET':
       return render(request, 'appointment/addappointment.html', {'form': form}) 


def allappointments(request):
    appointments = Appointment.objects.order_by('-date_added')
    return render(request, 'appointment/allappointments.html', {'appointments': appointments})


def deleteappointment(request, apt_pk):
    try:
        apttodelete = get_object_or_404(Appointment, pk=apt_pk)
        apttodelete.delete()
        messages.add_message(request, messages.SUCCESS, 'Appointment deleted successfully!')
        return redirect('allappointments')
    except:
        messages.add_message(request, messages.ERROR, 'Something went wrong! Try again later!')
        return redirect('allappointments')


# for autocomplete feature in add add appointment form
def fetchpatientnames(request):
    if 'term' in request.GET:
        patients = Patient.objects.filter(full_name__icontains=request.GET.get('term'))
        names = list()
        for patient in patients:
            names.append(patient.full_name)
        return JsonResponse(names, safe=False)

