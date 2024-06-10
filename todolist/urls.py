from django.urls import path

from . import views

urlpatterns = [
    path('todolist/', views.todolist, name='todolist'),
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete/<task_id>/', views.delete, name='delete'),
    path('edit/<task_id>/', views.edit, name='edit'),
    path('complete/<task_id>/', views.complete, name='complete'),
    path('pending/<task_id>/', views.pending, name='pending'),
    path('session/', views.session, name='session'),
]
