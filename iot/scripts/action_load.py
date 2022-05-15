from apps.employee.models import Employee
from apps.action.models import Action

import csv


def run():
    with open('scripts/action/action.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        # Employee.objects.all().delete()
        Action.objects.all().delete()

        for row in reader:
            print(row)

            # status, _ = Action_status.objects.get_or_create(action=row[-1])
            employee, _ = Employee.objects.get_or_create(email=row[-1])

            action = Action(name=row[0],
                        date=row[1],
                        time_from=row[2],
                        time_to=row[3],
                        status=row[4],
                        employee=employee)
            action.save()