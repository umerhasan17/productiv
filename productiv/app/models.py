from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Reminder(models.Model):
    time = models.DateTimeField(editable=True, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Reminder(" + str(self.time) + ", " + self.place + ")"

    def __repr__(self):
        return self.__str__()


class Action(models.Model):
    description = models.CharField(max_length=1000)
    time = models.DateTimeField(editable=True, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Action(" + self.description + ", " + str(self.time) + ", " + self.place + ")"

    def __repr__(self):
        return self.__str__()

class Due(models.Model):
    time = models.DateTimeField(editable=True, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Due(" + str(self.time) + ", " + self.place + ")"

    def __repr__(self):
        return self.__str__()

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
    action = models.OneToOneField(Action, on_delete=models.CASCADE, null=True)
    is_complete = models.BooleanField(default=False)
    due = models.OneToOneField(Due, on_delete=models.CASCADE, null=True)
    reminder = models.OneToOneField(Reminder, on_delete=models.CASCADE, null=True)
    priority = models.IntegerField(default=2, validators=[MaxValueValidator(3), MinValueValidator(1)])
    # todo duration as list of from-to time
    # todo dependencies

    def __str__(self):
        return "Activity(" + str(self.reminder) + ", " + str(self.action) + ", " + str(self.due) + ")"

    def __repr__(self):
        return self.__str__()
