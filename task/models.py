from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=modeld.CASCADE, deafult=1)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TodoList list'
        verbose_name_plural = 'TodoList lists'
        ordering = ['-date_created']
