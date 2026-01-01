from django.db import models

from core.models import TimeStampedModelMixin


class Post(TimeStampedModelMixin):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE, related_name="posts")
    mentioned_users = models.ManyToManyField("account.User", related_name="mentioned_posts")

    content = models.TextField()
    image = models.ImageField(upload_to="posts/")
    