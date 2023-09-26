from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# local things
from hospital.models import Doctor, Specialization, Patient


# Create your models here.

class Department(models.Model):
    class Meta:
        ordering = ['-created_at']
    name = models.CharField(max_length=100)
    head_doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specialization)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_all_beds(self):
        """Fetches all beds belonging to Department"""
        return self.bed_set.prefetch_related('department')
    
    def get_all_admissions(self):
        """Fetches all admissions belongning to Department"""
        return self.admission_set.prefetch_related('department')


class Bed(models.Model):
    class Meta:
        ordering = ['number']
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    number = models.PositiveBigIntegerField(default=1, unique=True)
    AVAILABILTY_CHOICES = (
        ('available', "Available"),
        ('occupied', "Occupied"),
    )
    availability = models.CharField(max_length=9, choices=AVAILABILTY_CHOICES, 
                                    default='availabale')
    
    def __str__(self):
        return f"{self.number} - room"

    def get_all_admissions(self):
        """Fetches all admissions belonging to bed"""
        return self.admission_set.prefetch_related('bed')
    
    
class Admission(models.Model):
    class Meta:
        ordering = ['-created_at']
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient} | {self.room}"
    
    
class Invoice(models.Model):
    class Meta:
        ordering = ['-created_at']
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('partly_paid', "Partly paid"),
        ('paid', "Paid"),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    residual_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.patient} | {self.total_amount}"
    
    def get_all_payments(self):
        """Fetches all payments belonging to invoice"""
        return self.payment_set.prefetch_related('invoice')       
    

class Payment(models.Model):
    class Meta:
        ordering = ['-payed_at', 'invoice']
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    payed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"payment id: {self.id} | amount: {self.amount}"    



@receiver(post_save, sender=Payment)
def update_invoice_status(sender, instance, created, **kwargs):
    if created:
        invoice = instance.invoice
        
        """Updating the residual amount based on the total amount and associated payments"""
        total_payments = invoice.payment_set.aggregate(models.Sum('amount'))['amount__sum'] or 0.00
        invoice.residual_amount = max(invoice.total_amount - total_payments, 0.00)
        
        """Changing invoice status"""
        if invoice.residual_amount == 0.00:
            invoice.status = 'paid'
        elif invoice.residual_amount < invoice.total_amount:
            invoice.status = 'partly_paid'  
        invoice.save()