from django.urls import path
from rest_framework.routers import SimpleRouter 
from todos.views import TodoListCreateView, TodoRetrieveUpdateDeleteView


urlpatterns = [
    path('', TodoListCreateView.as_view()),
    path('<uuid:todo_id>/', TodoRetrieveUpdateDeleteView.as_view()),
]