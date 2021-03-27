from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SearchHistory(models.Model):
    user = models.ForeignKey(User, related_name='search_user', on_delete=models.CASCADE, blank=True, null=True)
    keyword = models.CharField(max_length=255)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword

    class Meta:
        ordering = ['-id']