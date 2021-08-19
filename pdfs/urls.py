from django.urls import path
from pdfs import views

urlpatterns = [
    path('<int:patient_pk>/investigationsreport/', views.investigationsreport, name='investigationsreport'),
    path('<int:patient_pk>/fertilitysheetpdf/', views.fertilitysheetpdf, name='fertilitysheetpdf'),
    path('<int:patient_pk>/malehistorypdf/', views.malehistorypdf, name='malehistorypdf'),
    path('<int:patient_pk>/wifeexamspdf/', views.wifeexamspdf, name='wifeexamspdf'),
    path('<int:patient_pk>/prescriptionpdf/', views.prescriptionpdf, name='prescriptionpdf'),

    path('<int:patient_pk>/ancsheetpdf/', views.ancsheetpdf, name='ancsheetpdf'),
    path('<int:patient_pk>/infsheetpdf/', views.infsheetpdf, name='infsheetpdf'),
    path('<int:patient_pk>/gynacsheetpdf/', views.gynacsheetpdf, name='gynacsheetpdf'),


    path('printrecords/', views.printrecords, name='printrecords'),

]