# urls.py
from django.urls import path
from . import views
urlpatterns = [
    path("todos", views.todos ,name="todos"),
    # path("todos/<int:pk>/", views.todo_details ,name="todos-details"),
]
