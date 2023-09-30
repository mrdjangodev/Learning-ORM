# from django
import time
from django.db import connection
from pprint import pprint

# from local
from departments.models import Department
from hospital.models import Patient, Doctor, Specialization
from .utils import (
    get_all_head_doctors, filter_doctors_by_currency_type, 
    filter_doctors_by_is_active_status, filter_all_appointments_by_status,
    get_all_doctors_belong_to_department, filter_beds_by_availabilty,
    filter_invoices_by_status,
                    )

def run():
    start_time = time.time()
    # head_doctors = get_all_head_doctors()
    # print(f"all head doctors: \n{head_doctors}")
    # doctors_by_currency = filter_doctors_by_currency_type('EUr')
    # doctors_by_actie_status = filter_doctors_by_is_active_status(False)
    # print(f"doctors_by_currency: \n{doctors_by_currency} \n\
    #     doctors_by_active_status: \n{doctors_by_actie_status}")
    
    # filtered_appointments = filter_all_appointments_by_status('scheduled')
    # print(f"Filtered appointments: \n{filtered_appointments}")
    
    # department = Department.objects.first()
    # retrived_doctors_by_department = get_all_doctors_belong_to_department(department)
    # pprint(f"retrived_doctors_by_department: {retrived_doctors_by_department}")
    
    # filtered_beds = filter_beds_by_availabilty('available')
    # pprint(f"{filtered_beds}")
    filtered_invoices = filter_invoices_by_status('PenDing')
    pprint(filtered_invoices)
    
    finish_time = time.time()
    print(f"Runtime: {finish_time-start_time}")
    pprint(connection.queries)