from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models. TextField(max_length = 500)
    is_completed = models.BooleanField(default = False)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'tasks')
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
    ROLES = (
        ('manager', 'Manager'),
        ('member', 'Member')
    )
    phone_number = models.CharField(max_length = 20, blank = True, null = True)
    role = models.CharField(max_length = 10, choices =ROLES, default = 'member')
    bio = models.TextField(max_length = 500, blank = True, null = True)

    def __str__(self):
        return f"{self.username}({self.role})"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    text = models.TextField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.task.title}"