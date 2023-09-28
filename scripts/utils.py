# from django



# from local
from hospital.models import Doctor
from departments.models import Department
from events.models import Appointment

def get_all_head_doctors():
    """retrieves all HeadDoctors"""
    # departments = Department.objects.select_related('head_doctor')
    # head_doctors = [department.head_doctor for department in departments]
    
    # commented code is not more afficient than uncommented one because
    # it has list comperhension and it involves an additional query to retrieve 
    # the departments and requires extra processing to extract the head doctors
    head_doctors = Doctor.objects.filter(department__isnull=False)
    return head_doctors


def filter_doctors_by_currency_type(currency_type:str):
    """
        available currencies : ['usd', 'uzs', 'eur']
    """
    return Doctor.objects.filter(salary_currency=currency_type.lower())


def filter_doctors_by_is_active_status(is_active:bool = True):
    return Doctor.objects.filter(is_active=is_active)


def filter_all_appointments_by_status(status:str):
    """filters all Appointments by status('scheduled', 'canceled', 'completed')

    Args:
        status (str): should be one of these ['scheduled', 'canceled', 'completed']
    """
    return Appointment.objects.select_related('doctor', 'patient').filter(status=status.lower())