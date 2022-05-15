from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Employee


class UserCreationForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = Employee
        fields = ('email',)
