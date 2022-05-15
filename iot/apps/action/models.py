from django.db import models
# from django.core.validators import MinValueValidator

from apps.employee.models import Employee


# Create your models here.
# class Action_status(models.Model):
#     WORKING = 1
#     CHATTING = 2
#     DRINKING_COFFEE = 3
#     TAKING_BREAK = 4
#     HELPING_COLLEAGUE = 5
#     ROLE_CHOICES = [
#         (WORKING, 'working'),
#         (CHATTING, 'chatting'),
#         (DRINKING_COFFEE, 'drinking_coffee'),
#         (TAKING_BREAK, 'taking_break'),
#         (HELPING_COLLEAGUE, 'helping_colleague'),
#     ]

#     id = models.PositiveSmallIntegerField(
#         primary_key=True, choices=ROLE_CHOICES)

#     def __str__(self):
#         return self.get_id_display()


class Action(models.Model):
    WORKING = 1
    CHATTING = 2
    DRINKING_COFFEE = 3
    TAKING_BREAK = 4
    HELPING_COLLEAGUE = 5
    ROLE_CHOICES = [
        (WORKING, 'working'),
        (CHATTING, 'chatting'),
        (DRINKING_COFFEE, 'drinking_coffee'),
        (TAKING_BREAK, 'taking_break'),
        (HELPING_COLLEAGUE, 'helping_colleague'),
    ]
    name = models.CharField(max_length=100)
    # type_of_action = models.CharField(max_length=255)
    date = models.DateField(null=True)
    time_from = models.TimeField(null=True)
    time_to = models.TimeField(null=True)
    status = models.CharField(max_length=20, choices=ROLE_CHOICES, default='working')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='action') 
    
    def __str__(self):
        return f"{self.name}"

    def get_fields(self):

        my_list = []

        for field in self.__class__._meta.fields[1:]:
            if field.verbose_name != 'employee':
                my_list.append(
                    (field.verbose_name, field.value_from_object(self)))
            else:
                my_list.append((field.verbose_name, Employee.objects.get(
                    pk=field.value_from_object(self)).employee))

        return my_list
