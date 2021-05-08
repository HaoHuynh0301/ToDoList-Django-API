from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ToDoView.as_view(), name = 'list_todo'),
    path('detail/<int:pk>/', views.ToDoDetailView.as_view(), name = 'detail')
]