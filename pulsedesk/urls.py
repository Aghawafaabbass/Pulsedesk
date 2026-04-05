from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect


def dashboard(request):
    if request.user.is_authenticated:
        return redirect('appointment_list')
    return redirect('login')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('patients/', include('patients.urls')),
    path('staff/', include('staff.urls')),
    path('appointments/', include('appointments.urls')),
]