from django.db import models
from core.models import TimeStampedModelMixin

class Comment(TimeStampedModelMixin):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)


