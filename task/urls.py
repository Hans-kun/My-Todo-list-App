from django.urls import path
from . views import *


urlpatterns = [
    path('', task_view, name='home'),
    path('update_task/<str:pk>/', updateView, name='update_task'),
    path('delete_task/<str:pk>/', deleteView, name='delete_task')
]
