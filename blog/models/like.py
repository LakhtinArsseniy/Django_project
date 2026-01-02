from django.db import models

from core.models import TimeStampedModelMixin


class Like(TimeStampedModelMixin):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, null=True, related_name='likes')
    comment = models.ForeignKey('blog.Comment', on_delete=models.CASCADE, null=True, related_name='likes')
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, related_name='likes')

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                        models.Q(post__isnull=True, comment__isnull=False) |
                        models.Q(post__isnull=False, comment__isnull=True)
                ),
                name='post_or_comment_is_set'
            ),
        ]