# from django



# from local
from hospital.models import Doctor
from departments.models import Department


def get_all_head_doctors():
    # departments = Department.objects.select_related('head_doctor')
    # head_doctors = [department.head_doctor for department in departments]
    head_doctors = Doctor.objects.filter(department__isnull=False)
    return head_doctors
    