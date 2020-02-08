from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class ActivityList(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def create(cls, name):
        return cls(name=name)

    def __str__(self):
        return self.name

def get_or_create_inbox():
    try:
        return ActivityList.objects.get(name="inbox")
    except:
        new_inbox = ActivityList.create("inbox")
        new_inbox.save()
        return new_inbox

class Activity(models.Model):
    parent_list = models.ForeignKey(ActivityList, on_delete=models.CASCADE, default=get_or_create_inbox) 
    description = models.CharField(max_length=1000, blank=True)
    is_complete = models.BooleanField(default=False)
    due_dt = models.DateTimeField(editable=True, blank=True, null=True)
    reminder_dt = models.DateTimeField(editable=True, blank=True, null=True)
    priority = models.IntegerField(default=2, validators=[MaxValueValidator(3), MinValueValidator(1)])
    # todo duration as list of from-to time
    # todo location 
    # todo dependencies

    
