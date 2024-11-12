from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer, TodoCreateSerializer
from .services import create_todo, get_todo_by_id, update_todo, delete_todo_by_id

class TodoListCreateView(generics.GenericAPIView):
    serializer_class = TodoCreateSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            todos = Todo.objects.filter(user=request.user)
            if not todos.exists():
                return Response({"detail": "No todos found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            todo = create_todo(serializer.validated_data, request.user)
            return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TodoRetrieveUpdateDeleteView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoCreateSerializer

    def get(self, request, todo_id):
        try:
            todo = get_todo_by_id(todo_id, request.user)
            if todo:
                return Response(TodoSerializer(todo).data)
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, todo_id):
        try:
            todo = get_todo_by_id(todo_id, request.user)
            if todo:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                todo = update_todo(todo, serializer.validated_data)
                return Response(TodoSerializer(todo).data)
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, todo_id):
        try:
            todo = get_todo_by_id(todo_id, request.user)
            if todo:
                delete_todo_by_id(todo_id, request.user)
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
