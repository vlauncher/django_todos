from .models import Todo
from django.db import transaction
from rest_framework.exceptions import NotFound

def get_todo_by_id(todo_id, user):
    try:
        return Todo.objects.get(id=todo_id, user=user)
    except Todo.DoesNotExist:
        raise NotFound(detail="Todo with the specified ID not found.")

@transaction.atomic
def create_todo(data, user):
    todo = Todo.objects.create(user=user, **data)
    return todo

@transaction.atomic
def update_todo(todo, data):
    for field, value in data.items():
        setattr(todo, field, value)
    todo.save()
    return todo

@transaction.atomic
def delete_todo_by_id(todo_id, user):
    todo = get_todo_by_id(todo_id, user)
    todo.delete()
    return todo
