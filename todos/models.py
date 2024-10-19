from django.db import models
from users.models import User


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'todos'
        ordering = ['-id']

    def __str__(self):
        return self.title
