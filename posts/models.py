from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_user', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title