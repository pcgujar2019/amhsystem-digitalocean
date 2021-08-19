from django.urls import path
from appointment import views

urlpatterns = [
    # Appointment related
    path('addappointment/', views.addappointment, name='addappointment'),
    path('allappointments/', views.allappointments, name='allappointments'),
    path('deleteappointment/<int:apt_pk>', views.deleteappointment, name='deleteappointment'),
    # path('viewpatient/<int:patient_pk>', views.viewpatient, name='viewpatient'),
    path('fetchpatientnames', views.fetchpatientnames, name='fetchpatientnames'),

]