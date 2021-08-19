from django.urls import path
from records import views

urlpatterns = [
    path('<int:patient_pk>/ancfirstblock', views.ancfirstblock, name='ancfirstblock'),
    path('<int:patient_pk>/ancotherblocks/<int:visit_no>', views.ancotherblocks, name='ancotherblocks'),


    path('<int:patient_pk>/infplanonefirstblock', views.infplanonefirstblock, name='infplanonefirstblock'),
    path('<int:patient_pk>/infplantwofirstblock', views.infplantwofirstblock, name='infplantwofirstblock'),
    path('<int:patient_pk>/infplanoneotherblocks/<int:visit_no>', views.infplanoneotherblocks, name='infplanoneotherblocks'),
    path('<int:patient_pk>/infplantwootherblocks/<int:visit_no>', views.infplantwootherblocks, name='infplantwootherblocks'),


    path('<int:patient_pk>/gynacfirstblock', views.gynacfirstblock, name='gynacfirstblock'),
    path('<int:patient_pk>/gynacotherblocks/<int:visit_no>', views.gynacotherblocks, name='gynacotherblocks'),


    path('<int:patient_pk>/investigations', views.investigations, name='investigations'),
    path('<int:patient_pk>/usg', views.usg, name='usg'),
    path('<int:patient_pk>/ttdose', views.ttdose, name='ttdose'),
    path('<int:patient_pk>/fertilitysheet', views.fertilitysheet, name='fertilitysheet'),
    path('<int:patient_pk>/malehistory', views.malehistory, name='malehistory'),
    path('<int:patient_pk>/wifeexams', views.wifeexams, name='wifeexams'),
]