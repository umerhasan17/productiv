class Activity:
    def __init__(self, reminder, action, due):
        self.reminder = reminder
        self.action = action
        self.due = due

    def __str__(self):
        return "Activity(" + str(self.reminder) + ", " + str(self.action) + ", " + str(self.due) + ")"

    def __repr__(self):
        return self.__str__()

class Reminder:
    def __init__(self, time, place):
        self.time = time
        self.place = place

    def __str__(self):
        return "Reminder(" + str(self.time) + ", " + self.place + ")"

    def __repr__(self):
        return self.__str__()


class Action:
    def __init__(self, description, time, place):
        self.description = description
        self.time = time
        self.place = place

    def __str__(self):
        return "Action(" + self.description + ", " + str(self.time) + ", " + self.place + ")"

    def __repr__(self):
        return self.__str__()


class Due:
    def __init__(self, time, place):
        self.time = time
        self.place = place

    def __str__(self):
        return "Due(" + str(self.time) + ", " + self.place + ")"

    def __repr__(self):
        return self.__str__()