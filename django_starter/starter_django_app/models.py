from django.db import models

# Create your models here.
from django.db.models import Model


class User(models.Model):
    user_name = models.CharField(max_length=35)
    password = models.CharField(max_length=16)
    display_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)


class Follows(models.Model):
    to_be_followed = models.ManyToManyField(User)
    being_followed_by = models.ManyToManyField(User)


class Follower(models.Model):
    following_user = models.ForeignKey(Follows.being_followed_by)


class Followed_User(models.Model):
    user_followed = models.ForeignKey(Follows.to_be_followed)


class Tweet(models.Model):
    words = models.CharField(max_length=160)
    picture = models.ImageField()
    owner = models.ForeignKey(User)
    tag = models.ManyToManyField(User)
    video = models.FileField()


class Search(models.Model):
    search_term = models.CharField(max_length=160)


class Direct_Message(models.Model):
    message = models.TextField()
    owner = models.ForeignKey(User)


class Feed(models.Model):
    user_followed_tweet = models.ManyToManyField(user_followed.Tweet)