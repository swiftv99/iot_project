from django.urls import path
from . import views

app_name = 'action'


urlpatterns = [
    path('', views.RequestListView.as_view(), name='all'),
    path('<int:pk>/detail', views.RequestDetailView.as_view(),
         name='action_detail'),
    path('create/', views.RequestCreateView.as_view(),
         name='action_create'),
    path('<int:pk>/update/',
         views.RequestUpdateView.as_view(), name='action_update'),
    path('<int:pk>/delete/',
         views.RequestDeleteView.as_view(), name='action_delete'),
]
