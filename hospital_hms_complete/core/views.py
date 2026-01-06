from django.shortcuts import render
from .models import Doctor, Patient, Appointment

def dashboard(request):
    return render(request, 'dashboard.html', {
        'doctors': Doctor.objects.count(),
        'patients': Patient.objects.count(),
        'appointments': Appointment.objects.count(),
    })

def doctors(request):
    return render(request, 'doctors.html', {'doctors': Doctor.objects.all()})

def patients(request):
    return render(request, 'patients.html', {'patients': Patient.objects.all()})

def appointments(request):
    return render(request, 'appointments.html', {'appointments': Appointment.objects.all()})
