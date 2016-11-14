from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField()
  raiting = models.IntegerField()
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  likes = models.ManyToManyField(User)

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
