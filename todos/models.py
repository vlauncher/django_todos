from django.db import models
from users.models import User
from django.utils.text import slugify
from django.utils import timezone
import uuid

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{uuid.uuid4()}")
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.title} - {self.description}'