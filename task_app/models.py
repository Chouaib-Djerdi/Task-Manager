from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=False)
    manager = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}'
    