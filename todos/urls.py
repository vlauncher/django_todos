from django.urls import path

from todos.views import TodoCreateList, TodoDetail

urlpatterns = [
    path('todos/', TodoCreateList.as_view()),
    path('todos/<int:pk>/', TodoDetail.as_view()),
]