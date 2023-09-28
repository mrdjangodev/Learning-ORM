# from django
from django.db import connection
from pprint import pprint

# from local
from hospital.models import Patient, Doctor, Specialization
from .utils import get_all_head_doctors

def run():
    head_doctors = get_all_head_doctors()
    print(f"all head doctors: \n{head_doctors}")
    # for head_doctor in head_doctors:
    #     print(head_doctor.first_name)
    pprint(connection.queries)