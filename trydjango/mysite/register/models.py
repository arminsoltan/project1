from django.db import models
# Create your models here.

class User_Password(models.Model):
    username=models.CharField(max_length=100,default="")
    password=models.CharField(max_length=100,default="")

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
