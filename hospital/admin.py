from django.contrib import admin
from django.utils.html import format_html

# from local
from .models import Specialization, Doctor, Patient
# Register your models here.

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
admin.site.register(Specialization, SpecializationAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'specialization', 'contact_number', \
        'email', 'address', 'image_preview', 'is_active', 'joining_date', 'updated_at']
    list_editable = ['is_active']
    search_fields = ['id', 'first_name', 'last_name', 'specialization__name', 'contact_number', \
        'email', 'address', 'is_active', 'joining_date',]
    # filter_vertical = ['specialization']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return None
    image_preview.short_description = 'Image'
    
admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'date_of_birth', \
        'contact_number', 'email', 'address', 'insurance_provider', 'insurance_policy_number']
    
    search_fields = ['id', 'first_name', 'last_name', 'date_of_birth', \
        'contact_number', 'email', 'address', 'insurance_provider', 'insurance_policy_number']
admin.site.register(Patient, PatientAdmin)