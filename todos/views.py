from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from todos.services import get_todos, get_todo, create_todo, update_todo, delete_todo
from rest_framework import status
from todos.serializers import TodoSerializer
from todos.models import Todo

class TodoCreateList(GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request):
        return Response(get_todos(), status=status.HTTP_200_OK)

    def post(self, request):
        return Response(create_todo(request.data), status=status.HTTP_201_CREATED)


class TodoDetail(GenericAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, pk):
        return Response(get_todo(pk), status=status.HTTP_200_OK)

    def put(self, request, pk):
        return Response(update_todo(pk, request.data), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        return Response(delete_todo(pk), status=status.HTTP_204_NO_CONTENT)

