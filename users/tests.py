from django.test import TestCase
from django.db.utils import IntegrityError
from users.models import User


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password='testpassword'
        )
    
    def test_create_user(self):
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpassword'))
    
    def test_create_superuser(self):
        user = User.objects.create_superuser(
            first_name='Admin',
            last_name='User',
            email='admin@example.com',
            password='adminpassword'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
