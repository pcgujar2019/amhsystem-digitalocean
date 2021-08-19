from django.urls import path
from main import views

urlpatterns = [
    # Auth
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('', views.home, name='home'),

    # Patients related
    path('allpatients/', views.allpatients, name='allpatients'),
    path('searchpatient/', views.searchpatient, name='searchpatient'),
    path('addpatient/', views.addpatient, name='addpatient'),
    path('viewpatient/<int:patient_pk>', views.viewpatient, name='viewpatient'),
    path('editpatient/<int:patient_pk>', views.editpatient, name='editpatient'),
    path('deletepatient/<int:patient_pk>', views.deletepatient, name='deletepatient'),
    path('fetchpatientnames', views.fetchpatientnames, name='fetchpatientnames'),

]