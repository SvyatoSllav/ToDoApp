from django.urls import include, path

from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.delete_task, name='delete_task'),
    path('api/', include('api.urls'))
]
