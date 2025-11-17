from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.add_Task, name="add_Task"),
    
    # Mark_as_done Feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),
    
    # Mark_us_undone Feature
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name="mark_as_undone"),
    
    # Edit Feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    
    # Delete Feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
