from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название задачи')
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
