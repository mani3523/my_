from django.db import models

from django.contrib.auth.models import User

class Todolist(models.Model):
    id = models.AutoField(primary_key=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.task + "|" + str(self.done)
