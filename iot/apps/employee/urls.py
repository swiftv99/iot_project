from django.urls import path
from . import views

app_name = 'employee'


urlpatterns = [
    path('', views.UserListView.as_view(), name='all'),
    path('employee/<int:pk>/detail', views.UserDetailView.as_view(), name='employee_detail'),
    path('employee/create/', views.UserCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/',
         views.UserUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/',
         views.UserDeleteView.as_view(), name='employee_delete'),

]
