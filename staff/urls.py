from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('<int:staff_id>/', views.staff_detail, name='staff_detail'),
    path('add/', views.add_staff, name='add_staff'),
    path('<int:staff_id>/delete/', views.delete_staff, name='delete_staff'),
]