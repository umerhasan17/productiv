import nltk
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

separator_tags = ['CC', 'IN', 'MD', 'TO', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP']
reminders = ['remember', 'remind']

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


def categorize_verb(verb):
    if verb in reminders:
        return "REMINDER"
    return "ACTION"


def tokenize(sentence):
    tagged_words = tag(sentence)
    tokens = []
    curr = []
    for tagged in tagged_words:
        if tagged[1] in separator_tags:
            tokens.append(curr)
            curr = []
        curr.append(tagged)
    tokens.append(curr)
    tokens.remove([])
    return tokens


def word_token(word):
    if word in reminders:
        return "REMINDER"
    return "NONE"


print(tag("""Remind me to do my coursework at Imperial at five o'clock."""))
tokens = tokenize("""Remind me to do my coursework at Imperial at 5o'clock.""")
for token in tokens:
    print(token)

# first = wordnet.synsets("remind")[0]
# second = wordnet.synsets("reminder")[0]
# print(first.wup_similarity(second))