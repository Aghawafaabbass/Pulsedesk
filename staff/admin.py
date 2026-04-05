from django.contrib import admin
from .models import Staff, Department, Schedule


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'department', 'specialization', 'is_available')
    list_filter = ('role', 'department', 'is_available')
    search_fields = ('user__first_name', 'specialization', 'license_number')
    list_editable = ('is_available',)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('staff', 'day_of_week', 'start_time', 'end_time', 'is_available')
    list_filter = ('day_of_week', 'is_available')