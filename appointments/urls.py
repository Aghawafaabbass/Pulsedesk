from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('add/', views.add_appointment, name='add_appointment'),
    path('<int:appointment_id>/status/', views.update_status, name='update_status'),
    path('<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),
]