from django.db import models

# from packages
from ckeditor_uploader.fields import RichTextUploadingField

# from locals
from hospital.models import Patient, Doctor

# Create your models here.

class Appointment(models.Model):
    class Meta:
        ordering = ['date_time'] 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('scheduled', "Scheduled"),
        ('canceled', "Canceled"),
        ('completed', "Completed"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    
    def __str__(self):
        return f"Doctor: {self.doctor} & Patient: {self.patient} | date time: {self.date_time} | status: {self.status}"

    def get_all_lab_test(self):
        """Fetches all Labaratory tests belonging to itself"""
        return self.labaratory_test_set.prefetch_related('appointment')
    

class LabTest(models.Model):
    class Meta:
        verbose_name = 'Labaratory Test'
        verbose_name_plural = "Labaratory Tests"
        ordering = ['-created_at']
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name = 'labaratory_test')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name = 'labaratory_test')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name = 'labaratory_test')
    name = models.CharField(max_length=100)
    result = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medication = models.TextField()
    dosage = models.TextField()
    instruction = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient} | {self.medication}"
