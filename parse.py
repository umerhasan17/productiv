import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

separator_tags = ['CC', 'IN', 'MD', 'TO', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP']

class Token:
    def __init__(self, kind, text):
        self.kind = kind
        self.text = text

    def __str__(self):
        return "(" + self.kind + ": " + self.text + ")"


def tag(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged

def tokenize(sentence):
    tagged_words = tag(sentence)
    i = 0
    while i < len(words):
        token, i = token_at(i, words)
        print(token)


def token_at(i, words):
    token = word_token(words[i])
    s = words[i]
    i = i + 1
    while i < len(words) and word_token(words[i]) == "NONE":
        s = s + " " + words[i]
        i = i + 1
    return Token(token, s), i


def word_token(word):
    if word in reminders:
        return "REMINDER"
    return "NONE"


print(tag("""Remind me to do my coursework at Imperial at five o'clock."""))
