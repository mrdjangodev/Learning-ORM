# from django
from django.db import connection
from pprint import pprint

# from local
from hospital.models import Patient, Doctor, Specialization
from .utils import get_all_head_doctors, filter_doctors_by_currency_type, filter_doctors_by_is_active_status

def run():
    # head_doctors = get_all_head_doctors()
    # print(f"all head doctors: \n{head_doctors}")
    doctors_by_currency = filter_doctors_by_currency_type('EUr')
    doctors_by_actie_status = filter_doctors_by_is_active_status(False)
    print(f"doctors_by_currency: \n{doctors_by_currency} \n\
        doctors_by_actie_status: \n{doctors_by_actie_status}")
    pprint(connection.queries)