from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TodoList list'
        verbose_name_plural = 'TodoList lists'
        ordering = ['-date_created']
