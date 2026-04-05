from django.contrib import admin
from .models import Patient, MedicalRecord


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'health_card_number', 'blood_type', 'city', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'health_card_number')
    list_filter = ('blood_type', 'province')


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'created_by', 'created_at')
    search_fields = ('patient__user__first_name', 'diagnosis')