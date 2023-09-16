from django.contrib import admin

# from local
from .models import Appointment, LabTest, Prescription
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'patient', 'date_time', 'status']
    search_fields = ['doctor__first_name', 'doctor__last_namr', 'patient__first_name', 'patient__last_name']
    list_filter = ['status']
    list_editable = ['status']  
admin.site.register(Appointment, AppointmentAdmin)


class LabTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'patient', 'appointment', 'name', 'result', 'created_at']
    search_fields = ['doctor__first_name', 'doctor__last_namr', 'patient__first_name', 'patient__last_name'\
        'appointment__id', 'name']
admin.site.register(LabTest, LabTestAdmin)


class PresciptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'patient', 'appointment', 'created_at']
    search_fields = ['doctor__first_name', 'doctor__last_namr', 'patient__first_name', 'patient__last_name'\
        'appointment__id']
admin.site.register(Prescription, PresciptionAdmin)

