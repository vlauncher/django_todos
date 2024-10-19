from todos.models import Todo
from todos.serializers import TodoSerializer


def get_todos():
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return serializer.data

def get_todo(pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo)
    return serializer.data

def create_todo(data):
    serializer = TodoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors

def update_todo(pk, data):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo, data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors

def delete_todo(pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return