from django.contrib import admin


# from local
from .models import Department, Bed, Admission, Invoice, Payment

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'head_doctor', 'created_at']
    search_fields = ['name']
    filter_horizontal = ['specializations']
    list_display_links = ['head_doctor']
admin.site.register(Department, DepartmentAdmin)


class BedAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'number', 'availability']
    list_display_links = ['department']
    search_fields = ['department__name']
    list_filter = ['availability']
    list_editable = ['availability']
admin.site.register(Bed, BedAdmin)


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'patient', 'bed', 'created_at']
    list_display_links = ['department', 'patient', 'bed']
    search_fields = ['dpartment__name', 'patient__firstn_name', 'patient__last_name', 'bed__number']
admin.site.register(Admission, AdmissionAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'total_amount', 'residual_amount', 'created_at']
    list_display_links = ['patient']
    search_fields = ['id', 'patient__first_name', 'patient__last_name']
admin.site.register(Invoice, InvoiceAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'amount', 'payed_at']
    list_display_links = ['invoice']
    search_fields = ['id', 'invoice__patient__first_name', 'invoice__patient__last_name']
admin.site.register(Payment, PaymentAdmin)