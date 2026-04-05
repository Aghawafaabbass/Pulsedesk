from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('add/', views.add_patient, name='add_patient'),
    path('<int:patient_id>/record/add/', views.add_medical_record, name='add_medical_record'),
    path('<int:patient_id>/delete/', views.delete_patient, name='delete_patient'),
]