from productiv.app.activity import Reminder, Action, Due, Activity
from productiv.app.parser import tokenizer
from timefhuman import timefhuman
from datetime import datetime
from datetime import timedelta

priority_value = {"low": 0, "medium": 1, "high": 2}

def parse_time(time_string):
    # return time_string
    if time_string == "":
        return timefhuman("tomorrow")
    date = timefhuman(time_string)
    if not date:
        return None
    if date < datetime.now():
        return date + timedelta(days=1)
    return date


class ActivityBuilder:
    def __init__(self):
        self.reminder = None
        self.action = None
        self.due = None
        self.stage = "NONE"
        self.description = ""
        self.time = ""
        self.place = ""
        self.priority = 0

    def add_token(self, token):
        if token.kind in ['REMINDER', 'ACTION', 'DUE']:
            if self.stage != 'NULL':
                self.finalise_current()
                self.description = token.text()
            self.stage = token.kind
        elif token.kind == 'PLACE':
            self.place += token.text() + " "
        elif token.kind == 'TIME':
            self.time += token.text() + " "
        elif token.kind == 'PRIORITY':
            self.priority = priority_value[token.words[0][0].lower()]

    def finalise_current(self):
        if self.stage == 'REMINDER':
            self.reminder = Reminder(parse_time(self.time), self.place)
        elif self.stage == 'ACTION':
            self.action = Action(self.description, parse_time(self.time), self.place)
        elif self.stage == 'DUE':
            self.due = Due(parse_time(self.time), self.place)
        self.time = ""
        self.place = ""

    def build(self):
        self.finalise_current()
        return Activity(self.reminder, self.action, self.due)


def parse_activity(sentence):
    tokenized_sentence = tokenizer.split_sentence(sentence)
    builder = ActivityBuilder()
    for element in tokenized_sentence:
        builder.add_token(element)
    return builder.build()


print(parse_activity("""Remind me in my home at 3 to do my coursework at Imperial at five pm high due
                        tomorrow at 5pm"""))
