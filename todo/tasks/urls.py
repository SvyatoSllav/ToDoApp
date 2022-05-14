from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='list'),
    path('complete/<str:pk>/', views.complete_task, name='complete_task'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.delete_task, name='delete_task'),
]
