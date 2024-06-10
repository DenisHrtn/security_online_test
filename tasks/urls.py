from django.urls import path
from tasks.views import TaskListCreateView, TaskDetailView, TaskAssignView, MyTasksAPI, TaskCloseView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/assign/', TaskAssignView.as_view(), name='task-assign'),
    path('my-tasks/', MyTasksAPI.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/close/', TaskCloseView.as_view(), name='task-close'),
]
