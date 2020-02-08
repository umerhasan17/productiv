from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Activity(models.Model):
    description = models.CharField(max_length=1000)
    is_complete = models.BooleanField(default=False)
    due_dt = models.DateTimeField(editable=True)
    reminder_dt = models.DateTimeField(editable=True)
    priority = models.IntegerField(default=2, validators=[MaxValueValidator(3), MinValueValidator(1)])
    # todo duration as list of from-to time
    # todo location 
    # todo dependencies