from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    follows = models.ManyToManyField("self", related_name='followers')
    followers = models.ManyToManyField("self", related_name='following')

    def follow(self, user):
        user.followers.add(self)
        self.follows.add(user)

    def unfollow(self, user):
        user.followers.add(self)
        self.follows.remove(user)
        