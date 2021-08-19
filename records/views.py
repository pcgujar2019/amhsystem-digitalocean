from django.core.exceptions import ValidationError
from django.http import request
from appointment.models import Appointment
from main.models import Patient
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.contrib import messages
from .forms import *

# Create your views here.
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def fertilitysheet(request, patient_pk):
    form = FertilitySheetForm()
    patient = get_object_or_404(Patient, pk=patient_pk)
    existingForm = FertilitySheet.objects.all().filter(patient=patient).first()
    if request.method == 'GET':
        if existingForm:
            form = FertilitySheetForm(instance=existingForm)
            return render(request, 'records/fertilitysheet.html', {'form':form, 'isformexists': True, 'patient': patient})
        else:
            return render(request, 'records/fertilitysheet.html', {'form':form, 'isformexists': False, 'patient': patient})    

    elif 'save' in request.POST:
        form = FertilitySheetForm(request.POST)
        try:            
            if form.is_valid():
                fsone = form.save(commit=False)
                fsone.patient = patient
                fsone.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved successfully!')
                return render(request, 'records/fertilitysheet.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Try again later!')
            return redirect('fertilitysheet')


    elif 'update' in request.POST:
        try:
            form = FertilitySheetForm(request.POST, instance=existingForm)
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Data updated successfully!')  
            return render(request, 'records/fertilitysheet.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Try again later!')
            return redirect('fertilitysheet')


@login_required(login_url='loginuser')
def investigations(request, patient_pk):
    form = InvestigationForm()
    patient = get_object_or_404(Patient, pk=patient_pk)
    existingForm = Investigation.objects.all().filter(patient=patient).first()
    if request.method == 'GET':
        if existingForm:
            form = InvestigationForm(instance=existingForm)
            return render(request, 'records/investigations.html', {'form':form, 'isformexists': True, 'patient': patient})
        else:
            return render(request, 'records/investigations.html', {'form':form, 'isformexists': False, 'patient': patient})  

    elif 'save' in request.POST:
        try:
            form = InvestigationForm(request.POST)            
            if form.is_valid():
                newform = form.save(commit=False)
                newform.patient = patient
                newform.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved successfully!')  
                return render(request, 'records/investigations.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Try again later!')
            return redirect('investigations')

    elif 'update' in request.POST:
        try:
            form = InvestigationForm(request.POST, instance=existingForm)
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Data updated successfully!') 
            return redirect('investigations', patient_pk)
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong! Try again later!')
            return redirect('investigations')


@login_required(login_url='loginuser')
def usg(request, patient_pk):
    form = UsgForm()
    patient = get_object_or_404(Patient, pk=patient_pk)
    existingForm = Usg.objects.all().filter(patient=patient).first()
    if request.method == 'GET':
        if existingForm:
            form = UsgForm(instance=existingForm)
            return render(request, 'records/usg.html', {'form':form, 'isformexists': True, 'patient': patient})
        else:
            return render(request, 'records/usg.html', {'form':form, 'isformexists': False, 'patient': patient})    
    elif 'save' in request.POST:
        form = UsgForm(request.POST) 
        try:           
            if form.is_valid():
                newform = form.save(commit=False)
                newform.patient = patient
                newform.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved successfully!') 
                return render(request, 'records/usg.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return render(request, 'records/usg.html', {'form':form, 'isformexists': True, 'patient': patient})

    elif 'update' in request.POST:
        try:
            form = UsgForm(request.POST, instance=existingForm)
            if form.is_valid():
                form.save()  
                messages.add_message(request, messages.SUCCESS, 'Data updated successfully!') 
                return render(request, 'records/usg.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return redirect('usg', patient_pk)    






@login_required(login_url='loginuser')
def ttdose(request, patient_pk):
    form = TtDoseForm()
    patient = get_object_or_404(Patient, pk=patient_pk)
    existingForm = TtDose.objects.all().filter(patient=patient).first()
    if request.method == 'GET':
        if existingForm:
            form = TtDoseForm(instance=existingForm)
            return render(request, 'records/ttdose.html', {'form':form, 'isformexists': True, 'patient': patient})
        else:
            return render(request, 'records/ttdose.html', {'form':form, 'isformexists': False, 'patient': patient})    
    elif 'save' in request.POST:
        form = TtDoseForm(request.POST) 
        try:           
            if form.is_valid():
                newform = form.save(commit=False)
                newform.patient = patient
                newform.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved successfully!') 
                return render(request, 'records/ttdose.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return render(request, 'records/ttdose.html', {'form':form, 'isformexists': True, 'patient': patient})

    elif 'update' in request.POST:
        try:
            form = TtDoseForm(request.POST, instance=existingForm)
            if form.is_valid():
                form.save()  
                messages.add_message(request, messages.SUCCESS, 'Data updated successfully!') 
                return render(request, 'records/ttdose.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return redirect('ttdose', patient_pk) 





















@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def malehistory(request, patient_pk):
    form = MaleMedicalHistoryForm()
    patient = get_object_or_404(Patient, pk=patient_pk)
    existingForm = MaleMedicalHistory.objects.all().filter(patient=patient).first()
    if request.method == 'GET':
        if existingForm:
            form = MaleMedicalHistoryForm(instance=existingForm)
            return render(request, 'records/malehistory.html', {'form':form, 'isformexists': True, 'patient': patient})
        else:
            return render(request, 'records/malehistory.html', {'form':form, 'isformexists': False, 'patient': patient})    
    elif 'save' in request.POST:
        try:
            form = MaleMedicalHistoryForm(request.POST)            
            if form.is_valid():
                newform = form.save(commit=False)
                newform.patient = patient
                newform.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved successfully!') 
                return render(request, 'records/malehistory.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
                messages.add_message(request, messages.ERROR, 'Something went wrong!') 
                return redirect('malehistory')


    elif 'update' in request.POST:
        try:
            form = MaleMedicalHistoryForm(request.POST, instance=existingForm)
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Data updated successfully!')  
            return render(request, 'records/malehistory.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!') 
            return redirect('malehistory')


@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def wifeexams(request, patient_pk):
    form = WifeExaminationForm()
    patient = get_object_or_404(Patient, pk=patient_pk)
    existingForm = WifeExamination.objects.all().filter(patient=patient).first()
    if request.method == 'GET':
        if existingForm:
            form = WifeExaminationForm(instance=existingForm)
            return render(request, 'records/wifeexams.html', {'form':form, 'isformexists': True, 'patient': patient})
        else:
            return render(request, 'records/wifeexams.html', {'form':form, 'isformexists': False, 'patient': patient})    
    elif 'save' in request.POST:
        try:
            form = WifeExaminationForm(request.POST)            
            if form.is_valid():
                newform = form.save(commit=False)
                newform.patient = patient
                newform.save()
                messages.add_message(request, messages.SUCCESS, 'Data saved successfully!')
                return render(request, 'records/wifeexams.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!') 
            return redirect('wifeexams')

    elif 'update' in request.POST:
        try:
            form = WifeExaminationForm(request.POST, instance=existingForm)
            form.save()  
            messages.add_message(request, messages.SUCCESS, 'Data saved successfully!') 
            return render(request, 'records/wifeexams.html', {'form':form, 'isformexists': True, 'patient': patient})
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!') 
            return redirect('wifeexams')





























# ========================Create appointment, Update appointment ================================


def createAppointment(patient, visit_no, on_date):
    date = datetime.strptime(on_date, "%d-%m-%Y").strftime('%Y-%m-%d')
    isAptExist = Appointment.objects.filter(on_date=date, patient=patient, visit_no=visit_no)
    if isAptExist:
        pass
    else:
        try:
            Appointment.objects.create(
                patient = patient,
                patient_name = patient.full_name,
                on_date = date,
                visit_no = visit_no
                )
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!') 

def updateAppointment(patient, visit_no, on_date):
    date = datetime.strptime(on_date, "%d-%m-%Y").strftime('%Y-%m-%d')
    apt = Appointment.objects.filter(patient=patient, visit_no=visit_no)
    apt.update(on_date=date)

















# ============================= ANC FIRST BLOCK ==========================
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def ancfirstblock(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = AncOpdFirstBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit no (for button)
    newformnumber = 2

    otherformsset = AncOpdBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = AncOpdFirstBlock.objects.filter(patient=patient, visit_no=1).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = AncOpdFirstBlockForm(instance=oldmainform)
        else:
            mainform = AncOpdFirstBlockForm()
        return render(request, 'records/ancfirstblock.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            })

    elif 'mainblocksave' in request.POST:
        mainform = AncOpdFirstBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('ancfirstblock', patient_pk)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, e)
            return redirect('ancfirstblock', patient_pk)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = AncOpdFirstBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('ancfirstblock', patient_pk)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return redirect('ancfirstblock', patient_pk)






# ============================= ANC OTHER BLOCKS ==========================
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def ancotherblocks(request, patient_pk, visit_no):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = AncOpdBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit no (for button)
    newformnumber = 2

    # Get first block (visit no-1) date added (for navigation buttons)
    visit_no_1_date = AncOpdFirstBlock.objects.filter(patient=patient).first().date_added

    otherformsset = AncOpdBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = AncOpdBlock.objects.filter(patient=patient, visit_no=visit_no).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = AncOpdBlockForm(instance=oldmainform)
        else:
            mainform = AncOpdBlockForm()
        return render(request, 'records/ancotherblocks.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            'visit_no': visit_no,
            'visit_no_1_date': visit_no_1_date
            })

    elif 'mainblocksave' in request.POST:
        mainform = AncOpdBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('ancotherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return redirect('ancotherblocks', patient_pk=patient_pk, visit_no=visit_no)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = AncOpdBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('ancotherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return redirect('ancotherblocks', patient_pk=patient_pk, visit_no=visit_no)

















# ============================= GYNAC FIRST BLOCK ==========================
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def gynacfirstblock(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = GynacOpdFirstBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit no (for button)
    newformnumber = 2

    otherformsset = GynacOpdBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = GynacOpdFirstBlock.objects.filter(patient=patient, visit_no=1).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = GynacOpdFirstBlockForm(instance=oldmainform)
        else:
            mainform = GynacOpdFirstBlockForm()
        return render(request, 'records/gynacfirstblock.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            })

    elif 'mainblocksave' in request.POST:
        mainform = GynacOpdFirstBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('gynacfirstblock', patient_pk)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, e)
            return redirect('gynacfirstblock', patient_pk)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = GynacOpdFirstBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('gynacfirstblock', patient_pk)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid dataaaaa!')
            return redirect('gynacfirstblock', patient_pk)


# ============================= GYNAC OTHER BLOCKS ==========================
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def gynacotherblocks(request, patient_pk, visit_no):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = GynacOpdBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit no (for button)
    newformnumber = 2

    # Get first block (visit no-1) date added (for navigation buttons)
    visit_no_1_date = GynacOpdFirstBlock.objects.filter(patient=patient).first().date_added

    otherformsset = GynacOpdBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = GynacOpdBlock.objects.filter(patient=patient, visit_no=visit_no).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = GynacOpdBlockForm(instance=oldmainform)
        else:
            mainform = GynacOpdBlockForm()
        return render(request, 'records/gynacotherblocks.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            'visit_no': visit_no,
            'visit_no_1_date': visit_no_1_date
            })

    elif 'mainblocksave' in request.POST:
        mainform = GynacOpdBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('gynacotherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return redirect('gynacotherblocks', patient_pk=patient_pk, visit_no=visit_no)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = GynacOpdBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('gynacotherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return redirect('gynacotherblocks', patient_pk=patient_pk, visit_no=visit_no)












# ============================= INF PLAN 1 - FIRST BLOCK ==========================
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def infplanonefirstblock(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = InfPlanOneFirstBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit number (for button)
    newformnumber = 2

    otherformsset = InfPlanOneBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = InfPlanOneFirstBlock.objects.filter(patient=patient, visit_no=1).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = InfPlanOneFirstBlockForm(instance=oldmainform)
        else:
            mainform = InfPlanOneFirstBlockForm()
        return render(request, 'records/infplanonefirstblock.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            })

    elif 'mainblocksave' in request.POST:
        mainform = InfPlanOneFirstBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('infplanonefirstblock', patient_pk)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, e)
            return redirect('infplanonefirstblock', patient_pk)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = InfPlanOneFirstBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('infplanonefirstblock', patient_pk)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid dataaaaa!')
            return redirect('infplanonefirstblock', patient_pk)




# ============================= INF PLAN ONE OTHER BLOCKS ==========================
def infplanoneotherblocks(request, patient_pk, visit_no):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = InfPlanOneBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit no (for button)
    newformnumber = 2

    # Get first block (visit no-1) date added (for navigation buttons)
    visit_no_1_date = InfPlanOneFirstBlock.objects.filter(patient=patient).first().date_added

    otherformsset = InfPlanOneBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = InfPlanOneBlock.objects.filter(patient=patient, visit_no=visit_no).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = InfPlanOneBlockForm(instance=oldmainform)
        else:
            mainform = InfPlanOneBlockForm()
        return render(request, 'records/infplanoneotherblocks.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            'visit_no': visit_no,
            'visit_no_1_date': visit_no_1_date
            })

    elif 'mainblocksave' in request.POST:
        mainform = InfPlanOneBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('infplanoneotherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return redirect('infplanoneotherblocks', patient_pk=patient_pk, visit_no=visit_no)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = InfPlanOneBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('infplanoneotherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return redirect('infplanoneotherblocks', patient_pk=patient_pk, visit_no=visit_no)





















# ============================= INF PLAN 2 - FIRST BLOCK ==========================
@login_required(login_url='loginuser')
@permission_required('main.delete_patient')
def infplantwofirstblock(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = InfPlanTwoFirstBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit number (for button)
    newformnumber = 2

    otherformsset = InfPlanTwoBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = InfPlanTwoFirstBlock.objects.filter(patient=patient, visit_no=1).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = InfPlanTwoFirstBlockForm(instance=oldmainform)
        else:
            mainform = InfPlanTwoFirstBlockForm()
        return render(request, 'records/infplantwofirstblock.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            })

    elif 'mainblocksave' in request.POST:
        mainform = InfPlanTwoFirstBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('infplantwofirstblock', patient_pk)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, e)
            return redirect('infplantwofirstblock', patient_pk)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = InfPlanTwoFirstBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('infplantwofirstblock', patient_pk)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid dataaaaa!')
            return redirect('infplantwofirstblock', patient_pk)




# ============================= INF PLAN 2 OTHER BLOCKS ==========================
def infplantwootherblocks(request, patient_pk, visit_no):
    patient = get_object_or_404(Patient, pk=patient_pk)
    mainform = InfPlanTwoBlockForm()

    ismainform = False
    otherforms = []

     # To get the next blank visit no (for button)
    newformnumber = 2

    # Get first block (visit no-1) date added (for navigation buttons)
    visit_no_1_date = InfPlanTwoFirstBlock.objects.filter(patient=patient).first().date_added

    otherformsset = InfPlanTwoBlock.objects.all().filter(patient=patient)
    if otherformsset:
        for otherform in otherformsset: 
            otherforms.append(otherform)
            newformnumber += 1
    oldmainform = InfPlanTwoBlock.objects.filter(patient=patient, visit_no=visit_no).first()

    if request.method == 'GET':
        if oldmainform:
            ismainform = True
            mainform = InfPlanTwoBlockForm(instance=oldmainform)
        else:
            mainform = InfPlanTwoBlockForm()
        return render(request, 'records/infplantwootherblocks.html', {
            'patient':patient, 
            'mainform': mainform, 
            'otherforms':otherforms,
            'ismainform': ismainform,
            'newformnumber': newformnumber,
            'visit_no': visit_no,
            'visit_no_1_date': visit_no_1_date
            })

    elif 'mainblocksave' in request.POST:
        mainform = InfPlanTwoBlockForm(request.POST)
        try: 
            if mainform.is_valid():
                newmainform = mainform.save(commit=False)

                #  create appointment based on flu date & visit no
                on_date = request.POST['flu_date']
                visit_no = request.POST['visit_no']
                createAppointment(patient, visit_no, on_date)

                newmainform.patient = patient
                newmainform.save()
                messages.add_message(request, messages.SUCCESS, 'Data Saved Successfully!!')
                return redirect('infplantwootherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except Exception as e: 
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return redirect('infplantwootherblocks', patient_pk=patient_pk, visit_no=visit_no)

    elif 'mainblockupdate' in request.POST:
        try:
            on_date = request.POST['flu_date']
            visit_no = request.POST['visit_no']
            newmainform = InfPlanOneBlockForm(request.POST, instance=oldmainform)
            if newmainform.is_valid():
                newmainform.save()

            # update appointment - only on_date value  
            updateAppointment(patient, visit_no, on_date)
            messages.add_message(request, messages.SUCCESS, 'Data Updated Successfully!!')
            return redirect('infplantwootherblocks', patient_pk=patient_pk, visit_no=visit_no)
        except:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return redirect('infplantwootherblocks', patient_pk=patient_pk, visit_no=visit_no)