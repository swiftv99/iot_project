# from curses.ascii import EM
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Employee
    list_display = ('email', 'first_name', 'last_name', 'title', 'department', 'room',)
    list_filter = ('email', 'first_name', 'last_name', 'title', 'department', 'room',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
         'fields': ('first_name', 'last_name', 'title', 'department', 'room',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'title', 'department', 'room',)}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'title', 'department', 'room')
    ordering = ('email', 'first_name', 'last_name', 'title', 'department', 'room')


# Register your models here.
admin.site.register(Employee, CustomUserAdmin)

