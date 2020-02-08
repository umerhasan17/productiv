import tokenizer

priority_value = {"low": 0, "medium": 1, "high": 2}


class ActivityBuilder:
    def __init__(self):
        self.stage = "NONE"
        self.info = {"NONE": ([], [])}
        self.priority = 0

    def add_token(self, token):
        if token.kind in ['REMINDER', 'ACTION', 'DUE']:
            self.stage = token.kind
            self.info[self.stage] = ([], [])
        elif token.kind == 'PLACE':
            self.info[self.stage][1].append(token.text())
        elif token.kind == 'TIME':
            self.info[self.stage][0].append(token.text())
        elif token.kind == 'PRIORITY':
            self.priority = priority_value[token.words[0][0].lower()]

    def __str__(self):
        return "PRIORITY " + str(self.priority) + "\n" + str(self.info)


print(tokenizer.split_sentence("""Remind me at 3 at home to do my coursework at Imperial at five o'clock low due
                                  tomorrow at 5pm"""))

tokenized_sentence = tokenizer.split_sentence("""Remind me at home at 3 to do my coursework at Imperial
                                                 at five o'clock high due tomorrow at 5pm""")

builder = ActivityBuilder()
for element in tokenized_sentence:
    builder.add_token(element)
print(builder)
