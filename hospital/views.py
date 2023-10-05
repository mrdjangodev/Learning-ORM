from django.shortcuts import render

from .models import Doctor, Patient

# Create your views here.
def home(request):
    
    doctors = Doctor.objects.select_related('specialization')
    patients = Patient.objects.all()
    
    context = {
        'doctor_model': Doctor,
        'doctors': doctors,
        'patients': patients,
    }
    return render(request, 'index.html', context)