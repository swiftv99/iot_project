from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Create your models here.
class Employee(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=255, null=True)
    room = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def str(self):
        return f"{self.first_name} {self.last_name}"

    def get_fields(self):
        my_list = []

        for field in self.__class__._meta.fields[1:]:
            if field.verbose_name != 'role':
                my_list.append(
                    (field.verbose_name, field.value_from_object(self)))
            else:
                my_list.append((field.verbose_name, Employee.objects.get(
                    pk=field.value_from_object(self)).role))

        return my_list


