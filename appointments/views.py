from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import Appointment
from patients.models import Patient
from staff.models import Staff


@login_required
def appointment_list(request):
    appointments = Appointment.objects.all().select_related('patient__user', 'doctor__user')

    status_filter = request.GET.get('status', '')
    date_filter = request.GET.get('date', '')
    search = request.GET.get('q', '')

    if status_filter:
        appointments = appointments.filter(status=status_filter)
    if date_filter:
        appointments = appointments.filter(appointment_date=date_filter)
    if search:
        appointments = appointments.filter(
            Q(patient__user__first_name__icontains=search) |
            Q(patient__user__last_name__icontains=search) |
            Q(doctor__user__first_name__icontains=search)
        )

    stats = {
        'total': Appointment.objects.count(),
        'scheduled': Appointment.objects.filter(status='scheduled').count(),
        'confirmed': Appointment.objects.filter(status='confirmed').count(),
        'completed': Appointment.objects.filter(status='completed').count(),
        'cancelled': Appointment.objects.filter(status='cancelled').count(),
        'today': Appointment.objects.filter(appointment_date=timezone.now().date()).count(),
    }

    return render(request, 'appointments/appointment_list.html', {
        'appointments': appointments,
        'stats': stats,
        'status_filter': status_filter,
        'date_filter': date_filter,
        'search': search,
        'today': timezone.now().date(),
    })


@login_required
def add_appointment(request):
    patients = Patient.objects.all().select_related('user')
    doctors = Staff.objects.filter(role='doctor', is_available=True).select_related('user')

    if request.method == 'POST':
        Appointment.objects.create(
            patient_id=request.POST.get('patient'),
            doctor_id=request.POST.get('doctor'),
            appointment_date=request.POST.get('appointment_date'),
            appointment_time=request.POST.get('appointment_time'),
            appointment_type=request.POST.get('appointment_type', 'general'),
            status='scheduled',
            reason=request.POST.get('reason', ''),
            notes=request.POST.get('notes', ''),
        )
        messages.success(request, 'Appointment booked!')
        return redirect('appointment_list')

    return render(request, 'appointments/add_appointment.html', {
        'patients': patients,
        'doctors': doctors,
        'today': timezone.now().date(),
    })


@login_required
def update_status(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.status = request.POST.get('status', appointment.status)
        appointment.save()
        messages.success(request, 'Status updated!')
    return redirect('appointment_list')


@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    messages.success(request, 'Appointment deleted.')
    return redirect('appointment_list')