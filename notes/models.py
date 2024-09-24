from django.db import models
from django.contrib.auth.models import User  # Импортируем модель пользователя


class Theme(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем

    def __str__(self):
        return self.name

class Note(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
