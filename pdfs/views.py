from django.shortcuts import render
import datetime
import io
from django.http.response import JsonResponse
from main.models import Patient
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from records.models import *
from medicine.models import PrescriptionItem
from .forms import *
from datetime import date
# FOR PDF
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.
def investigationsreport(request, patient_pk):
    template_path = 'pdfs/investigationsreport.html'
    patient = get_object_or_404(Patient, pk=patient_pk)
    investigation = None
    usg = None
    ttdose = None
    investigationdata = Investigation.objects.all().filter(patient=patient).first()
    usgdata = Usg.objects.all().filter(patient=patient).first()
    ttdosedata = TtDose.objects.all().filter(patient=patient).first()

    if investigationdata:
        investigation = investigationdata
    if usgdata:
        usg = usgdata
    if ttdosedata:
        ttdose = ttdosedata 
    context = {'patient': patient, 'investigation': investigation, 'usg':usg, 'ttdose': ttdose}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # To download the PDF
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #  To only display PDF
    response['Content-Disposition'] = 'filename="investigations.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

    # create a pdf
    # pisa_status = pisa.CreatePDF(
    #    html, dest=response)
    # if error then show some funy view
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response









def fertilitysheetpdf(request, patient_pk):
    template_path = 'pdfs/fertilitysheetpdf.html'
    patient = get_object_or_404(Patient, pk=patient_pk)
    fertilitysheet = None
    fertilitysheetdata = FertilitySheet.objects.all().filter(patient=patient).first()
    if fertilitysheetdata:
        fertilitysheet = fertilitysheetdata
    context = {'patient': patient, 'fertilitysheet': fertilitysheet}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="fertilitysheet.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return













def malehistorypdf(request, patient_pk):
    template_path = 'pdfs/malehistorypdf.html'
    patient = get_object_or_404(Patient, pk=patient_pk)
    malehistory = None
    malehistorydata = MaleMedicalHistory.objects.all().filter(patient=patient).first()
    if malehistorydata:
        malehistory = malehistorydata
    context = {'patient': patient, 'malehistory': malehistory}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="malehistory.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return















def wifeexamspdf(request, patient_pk):
    template_path = 'pdfs/wifeexamspdf.html'
    patient = get_object_or_404(Patient, pk=patient_pk)
    wifeexams = None
    wifeexamsdata = WifeExamination.objects.all().filter(patient=patient).first()
    if wifeexamsdata:
        wifeexams = wifeexamsdata
    context = {'patient': patient, 'wifeexams': wifeexams}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="wifeexams.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return










# Get only today's prescriptions and convert to PDF
def prescriptionpdf(request, patient_pk):
    template_path = 'pdfs/prescriptionpdf.html'
    patient = get_object_or_404(Patient, pk=patient_pk)
    prescriptions = []
    today = date.today()

    prescriptionsdata = PrescriptionItem.objects.all().filter(patient=patient,
     date_prescribed=datetime.date(today.year,today.month,today.day))

    if prescriptionsdata:
        for p in prescriptionsdata:
            prescriptions.append(p)
    context = {'patient': patient, 'prescriptions': prescriptions}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="prescriptions.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return











# ANC Sheet convert to PDF
def ancsheetpdf(request, patient_pk):
    template_path = 'pdfs/ancsheetpdf.html'
    patient = get_object_or_404(Patient, pk=patient_pk)
    firstblock = None
    otherblocks = []

    firstblockdata = AncOpdFirstBlock.objects.filter(patient=patient).first()
    otherblocksdata = AncOpdBlock.objects.all().filter(patient=patient)

    if otherblocksdata:
        for p in otherblocksdata:
            otherblocks.append(p)
    if firstblockdata:
        firstblock = firstblockdata
    context = {'patient': patient, 'otherblocks': otherblocks, 'firstblock':firstblock}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="ancsheetpdf.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



# GYNAC Sheet convert to PDF
def gynacsheetpdf(request, patient_pk):
    template_path = 'pdfs/gynacsheetpdf.html'
    patient = get_object_or_404(Patient, pk=patient_pk)
    firstblock = None
    otherblocks = []

    firstblockdata = GynacOpdFirstBlock.objects.filter(patient=patient).first()
    otherblocksdata = GynacOpdBlock.objects.all().filter(patient=patient)

    if otherblocksdata:
        for p in otherblocksdata:
            otherblocks.append(p)
    if firstblockdata:
        firstblock = firstblockdata
    context = {'patient': patient, 'otherblocks': otherblocks, 'firstblock':firstblock}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="gynacsheetpdf.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return


def infsheetpdf(request, patient_pk):
    pass



def printrecords(request):
    if request.method == 'GET':
        return render(request, 'pdfs/printrecords.html')
    elif request.method == 'POST':
        patient = Patient.objects.all().filter(full_name = request.POST['query']).first()
        print(patient)
        return render(request, 'pdfs/printrecords.html', {'patient': patient})


# for autocomplete feature in add add appointment form
def fetchpatientnames(request):
    if 'term' in request.GET:
        patients = Patient.objects.filter(full_name__icontains=request.GET.get('term'))
        names = list()
        for patient in patients:
            names.append(patient.full_name)
        return JsonResponse(names, safe=False)