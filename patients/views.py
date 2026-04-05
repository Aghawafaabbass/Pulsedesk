from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Patient, MedicalRecord


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    search = request.GET.get('q', '')
    if search:
        patients = patients.filter(
            Q(user__first_name__icontains=search) |
            Q(user__last_name__icontains=search) |
            Q(health_card_number__icontains=search)
        )
    return render(request, 'patients/patient_list.html', {
        'patients': patients,
        'search': search
    })


@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    records = patient.medical_records.all().order_by('-created_at')
    appointments = patient.appointments.all().order_by('-appointment_date')
    return render(request, 'patients/patient_detail.html', {
        'patient': patient,
        'records': records,
        'appointments': appointments
    })


@login_required
def add_patient(request):
    from django.contrib.auth.models import User
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            Patient.objects.create(
                user=user,
                health_card_number=request.POST.get('health_card_number'),
                phone=request.POST.get('phone'),
                date_of_birth=request.POST.get('date_of_birth') or None,
                blood_type=request.POST.get('blood_type', ''),
                city=request.POST.get('city'),
                province=request.POST.get('province'),
                postal_code=request.POST.get('postal_code'),
                emergency_contact_name=request.POST.get('emergency_contact_name'),
                emergency_contact_phone=request.POST.get('emergency_contact_phone'),
            )
            messages.success(request, f'Patient {first_name} {last_name} added!')
            return redirect('patient_list')
    return render(request, 'patients/add_patient.html')


@login_required
def add_medical_record(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        MedicalRecord.objects.create(
            patient=patient,
            diagnosis=request.POST.get('diagnosis'),
            prescription=request.POST.get('prescription', ''),
            notes=request.POST.get('notes', ''),
            created_by=request.user
        )
        messages.success(request, 'Medical record added!')
        return redirect('patient_detail', patient_id=patient.id)
    return render(request, 'patients/add_record.html', {'patient': patient})


@login_required
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.user.delete()
    messages.success(request, 'Patient deleted.')
    return redirect('patient_list')