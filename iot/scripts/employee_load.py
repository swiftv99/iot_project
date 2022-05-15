from apps.employee.models import Employee
import csv


def run():
    with open('scripts/employee/employee.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Employee.objects.all().delete()
        # Action.objects.all().delete()

        for row in reader:
            print(row)


            action = Employee(email=row[0],
                        first_name=row[1],
                        last_name=row[2],
                        title=row[3],
                        department=row[4],
                        room=row[5],)
            action.save()