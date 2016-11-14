from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
  def new(self):
    return super(QuestionManager, self).get_query_set().all().order_by('-added_at')

  def popular(self):
    return super(QuestionManager, self).get_query_set().all().order_by('-rating')


class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField()
  rating = models.IntegerField()
  author = models.ForeignKey(User, null=True, related_name='author', on_delete=models.SET_NULL)
  likes = models.ManyToManyField(User, related_name='likes')
  objects = QuestionManager()

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

