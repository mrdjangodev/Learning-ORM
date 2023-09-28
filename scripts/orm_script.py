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
    get_all_doctors_belong_to_department,
                    )

def run():
    # head_doctors = get_all_head_doctors()
    # print(f"all head doctors: \n{head_doctors}")
    # doctors_by_currency = filter_doctors_by_currency_type('EUr')
    # doctors_by_actie_status = filter_doctors_by_is_active_status(False)
    # print(f"doctors_by_currency: \n{doctors_by_currency} \n\
    #     doctors_by_active_status: \n{doctors_by_actie_status}")
    
    # filtered_appointments = filter_all_appointments_by_status('scheduled')
    # print(f"Filtered appointments: \n{filtered_appointments}")
    
    department = Department.objects.first()
    start_time = time.time()
    retrived_doctors_by_department = get_all_doctors_belong_to_department(department)
    finish_time = time.time()
    print(f"Runtime: {finish_time-start_time}")
    pprint(f"retrived_doctors_by_department: {retrived_doctors_by_department}")
    pprint(connection.queries)