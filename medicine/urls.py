from django.urls import path
from medicine import views

urlpatterns = [
    path('allmedicines/', views.allmedicines, name='allmedicines'),
    path('addmedicine/', views.addmedicine, name='addmedicine'),
    path('editmedicine/<int:medicine_pk>', views.editmedicine, name='editmedicine'),
    path('fetchmednames', views.fetchmednames, name='fetchmednames'),
    path('<int:patient_pk>/addprescription', views.addprescription, name='addprescription'),
    path('<int:patient_pk>/allprescriptions', views.allprescriptions, name='allprescriptions'),

]