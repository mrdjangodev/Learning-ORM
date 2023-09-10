from django.db import models

# from local
# from departments.models import Payment
# I'm removing this beccause of recycle importing error

# Create your models here.

class Specialization(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Doctor(models.Model):
    class Meta:
        ordering = ['-joining_date']
        
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=17)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250)
    image = models.ImageField(upload_to='doctors/')
    is_active = models.BooleanField(default=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    def get_all_appointments(self):
        """This function fetches and returns all appointments belong to the doctor"""
        return self.appointment_set.prefetch_related('doctor')
    
    def get_all_prescriptions(self):
        """This function fetches and returns all prescriptions belong to the doctor"""
        return self.prescription_set.prefetch_related('doctor')
    
    def get_all_lab_tests(self):
        """This function fetches and returns all labaratory tests belong to the doctor"""
        return self.labaratory_test_set.prefetch_related("doctor")
    
    
class Patient(models.Model):
    class Meta:
        ordering = ['first_name', 'last_name']
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=17)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200)
    insurance_provider = models.CharField(max_length=250)
    insurance_policy_number = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_all_admissions(self):
        """This function fetches and returns all admissions belong to the patient"""
        return self.appointment_set.prefetch_related('patient')
    
    def get_all_prescriptions(self):
        """This function fetches and returns all prescriptions belong to the patient"""
        return self.prescription_set.prefetch_related('patient')
    
    def get_all_lab_tests(self):
        """This function fetches and returns all labaratory tests belong to the patient"""
        return self.labaratory_test_set.prefetch_related("patient")
    
    def get_all_invoices(self):
        """This function fetches and returns all invoices belong to the patient"""
        return self.invoice_set.prefetch_related("patient")
    
    # def get_all_payments(self):
    #     """This function fetches and returns all payments belonging to the patient"""
    #     invoices = self.get_all_invoices()
    #     payments = Payment.objects.filter(invoice__in=invoices).select_related('invoice')
    #     return list(payments)   <- raised recycle error that is why I'm commenting it and 
    #     I'm gonna do it by another way
    
    def get_all_payments(self):
        # this is new way to fetch all payments belonging to the patient
        # it has little bit more steps and it might be slower than previous one 
        # but it is not raising recycle error
        """This function fetches and returns all payments belonging to the patient"""
        invoices = self.get_all_invoices()
        payments = []
        for invoice in invoices:
            invoice_paymnets = invoice.get_all_payments()
            payments.append(*invoice_paymnets)
        return payments