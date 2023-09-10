from django.db import models


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
        pass
    
    def get_all_admissions(self):
        """Fetches all admissions belongning to Department"""
        pass


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
    
    
class Amdission(models.Model):
    class Meta:
        ordering = ['-created_at']
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('scheduled', "Scheduled"),
        ('canceled', "Canceled"),
        ('completed', "Completed"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient} | {self.room}"
    
    
class Invoice(models.Model):
    class Meta:
        ordering = ['-created_at']
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.patient} | {self.total_amount}"
    
    def get_all_payments(self):
        """Fetches all payments belonging to invoice"""
        pass
    

class Payment(models.Model):
    class Meta:
        ordering = ['-payed_at', 'invoice']
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    payed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"payment id: {self.id} | amount: {self.amount}"    

    