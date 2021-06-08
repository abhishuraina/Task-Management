from django.urls import path
from . import views


urlpatterns = [
    path('', views.project_list, name = 'list'),

    path('<int:id>/', views.project_detail, name='detail'),
    path('<int:id>/task/', views.task_detail, name='tasks'),
    path('<int:id>/task/<int:pk>/', views.task_edit, name='tasks'),
]
