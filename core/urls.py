from django.urls import path
from .views import tasks_list, users_list

urlpatterns = [
    path('tasks/', tasks_list),
    path('users/', users_list),
]