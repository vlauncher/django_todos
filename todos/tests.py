from django.test import TestCase
from rest_framework.test import APIClient

from todos.models import Todo
from todos.serializers import TodoSerializer
from users.models import User


class TodoTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.todo = Todo.objects.create(user=self.user, title="Test Todo", description="Test Description")
        
    def test_get_todos(self):
        response = self.client.get('/api/v1/todos/')
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_todo(self):
        response = self.client.get('/api/v1/todos/1/')
        todo = Todo.objects.get(pk=1)
        serializer = TodoSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
    
    def test_create_todo(self):
        data = {
            "user": 1,
            "title": "Test Todo",
            "description": "Test Description"
        }
        response = self.client.post('/api/v1/todos/', data)
        self.assertEqual(response.status_code, 201)
    
    def test_update_todo(self):
        data = {
            "user": 1,
            "title": "Updated Todo",
            "description": "Updated Description"
        }
        response = self.client.put('/api/v1/todos/1/', data)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_todo(self):
        response = self.client.delete('/api/v1/todos/1/')
        self.assertEqual(response.status_code, 204)
    
    def test_get_todos_by_user(self):
        response = self.client.get('/api/v1/todos/?user=1')
        todos = Todo.objects.filter(user=1)
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
    
