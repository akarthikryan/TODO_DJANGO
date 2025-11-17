from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.add_Task, name="add_Task"),
]
