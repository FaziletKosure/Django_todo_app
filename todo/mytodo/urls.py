from django.urls import path
from . import views

urlpatterns = [
    path('', views.createTodo, name="list"),
    path('update/<int:id>/', views.updateTodo, name="update"),
    path('delete/<int:id>/', views.deleteTodo, name="delete"),
]
