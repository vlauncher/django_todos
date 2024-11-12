from django.test import TestCase
from todos.models import Todo
from users.models import User
from todos.serializers import TodoSerializer, TodoCreateSerializer
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status



class TodoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='todo_user@example.com',
            first_name='Todo',
            last_name='User',
            password='password'
        )
        self.todo = Todo.objects.create(
            user=self.user,
            title='Test Todo',
            description='Test description'
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.description, 'Test description')
        self.assertFalse(self.todo.completed)

    def test_todo_slug_autogeneration(self):
        self.todo.save()
        self.assertTrue(self.todo.slug)

    def test_todo_str(self):
        self.assertEqual(str(self.todo), 'Test Todo - Test description')

class TodoSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='serializer_user@example.com',
            first_name='Serializer',
            last_name='User',
            password='password'
        )
        self.todo = Todo.objects.create(
            user=self.user,
            title='Serialize Todo',
            description='Serialize description'
        )

    def test_todo_serializer(self):
        serializer = TodoSerializer(instance=self.todo)
        expected_data = {
            'id': str(self.todo.id),
            'title': 'Serialize Todo',
            'description': 'Serialize description',
            'completed': False,
            'slug': self.todo.slug,
            'user': self.user.id
        }
        self.assertEqual(serializer.data, expected_data)

    def test_todo_create_serializer(self):
        data = {
            'title': 'New Todo',
            'description': 'New description',
            'completed': False
        }
        serializer = TodoCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['title'], 'New Todo')

class TodoViewsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='view_user@example.com',
            first_name='View',
            last_name='User',
            password='password'
        )
        self.client.force_authenticate(user=self.user)
        self.todo = Todo.objects.create(
            user=self.user,
            title='View Todo',
            description='View description'
        )

    def test_get_todo_list(self):
        url = reverse('todo-list-create')
        response = self.client.get(url)
        todos = Todo.objects.filter(user=self.user)
        serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_todo(self):
        url = reverse('todo-list-create')
        data = {
            'title': 'New Test Todo',
            'description': 'New description',
            'completed': False
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])

    def test_retrieve_todo(self):
        url = reverse('todo-retrieve-update-delete', args=[str(self.todo.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo.title)

    def test_update_todo(self):
        url = reverse('todo-retrieve-update-delete', args=[str(self.todo.id)])
        data = {
            'title': 'Updated Todo',
            'description': 'Updated description',
            'completed': True
        }
        response = self.client.put(url, data)
        self.todo.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Todo')
        self.assertTrue(self.todo.completed)

    def test_delete_todo(self):
        url = reverse('todo-retrieve-update-delete', args=[str(self.todo.id)])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())