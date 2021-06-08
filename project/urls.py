from django.urls import path
from .views import ProjectList, TaskDetail, TaskList,  ProjectDetail



urlpatterns = [

    path('project/', ProjectList.as_view(), name='createProjects' ),

    path('project/<int:pk>/', ProjectDetail.as_view(), name='Projcts'),

    path('project/<int:pk>/task/', TaskList.as_view(), name='Tasks'),
    path('project/<int:id>/task/<int:pk>/', TaskDetail.as_view(), name='createTasks'),
    
]
