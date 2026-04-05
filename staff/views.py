from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Staff, Department, Schedule


@login_required
def staff_list(request):
    staff = Staff.objects.all().select_related('user', 'department')
    return render(request, 'staff/staff_list.html', {'staff': staff})


@login_required
def staff_detail(request, staff_id):
    member = get_object_or_404(Staff, id=staff_id)
    schedules = member.schedules.all()
    appointments = member.appointments.all().order_by('-appointment_date')[:10]
    return render(request, 'staff/staff_detail.html', {
        'member': member,
        'schedules': schedules,
        'appointments': appointments
    })


@login_required
def add_staff(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                password=request.POST.get('password')
            )
            Staff.objects.create(
                user=user,
                role=request.POST.get('role'),
                department_id=request.POST.get('department') or None,
                specialization=request.POST.get('specialization'),
                license_number=request.POST.get('license_number'),
                phone=request.POST.get('phone'),
                bio=request.POST.get('bio'),
            )
            messages.success(request, 'Staff member added!')
            return redirect('staff_list')
    return render(request, 'staff/add_staff.html', {'departments': departments})


@login_required
def delete_staff(request, staff_id):
    member = get_object_or_404(Staff, id=staff_id)
    member.user.delete()
    messages.success(request, 'Staff member deleted.')
    return redirect('staff_list')