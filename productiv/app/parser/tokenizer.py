import nltk

separator_tags = ['CC', 'IN', 'MD', 'TO', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP']
verb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
adjective_tags = ['JJ', 'JJR', 'JJS']
noun_tags = ['NN', 'NNP']

reminders = ['remember', 'remind']
times = ['tomorrow', 'today', 'noon', 'midnight']
priorities = ['low', 'medium', 'high']

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
               "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14",
               "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18", "nineteen": "19", "twenty": "20",
               "twenty-one": "21", "twentyone": "22", "twenty-two": "22", "twentytwo": "22", "twenty-three": "23",
               "twentythree": "23", "twenty-four": "24", "twentyfour": "24"}


class Token:
    def __init__(self, kind, words):
        self.kind = kind
        self.words = words

    def __str__(self):
        return "(" + self.kind + ": " + self.text() + ")"

    def __repr__(self):
        return self.__str__()

    def text(self):
        text = ""
        for word, kind in self.words:
            text += " " + word
        return text.strip()

"""
NLTK tokenization and parts of speech tagging
"""
def tokenize_and_tag(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged


def tokenize(sentence):
    tagged_words = tokenize_and_tag(sentence)
    elements = []
    curr = []
    for word, tag in tagged_words:
        if word in numbers:
            # convert word number to digit number
            tagged = (numbers[word], tag)
        if tag in separator_tags or word in priorities or word == 'due' or word in times:
            # create sentence segment
            elements.append(curr)
            curr = []
        curr.append(tagged)
    elements.append(curr)
    elements.remove([])
    return elements


def classify_word(token):
    word = token[0].lower()
    tag = token[1]

    if tag in verb_tags:
        if word in reminders:
            return "REMINDER"
        else:
            return "ACTION"
    if tag == 'CD' or word in times:
        return "TIME"
    if tag in noun_tags:
        return "PLACE"
    if word in priorities:
        return "PRIORITY"
    if word == "due":
        return "DUE"
    if word == 'to':
        return "TO"
    return "NONE"


def classify(element):
    for word in element:
        classification = classify_word(word)
        if classification is not "NONE":
            return classification
    return "NONE"


def split_sentence(sentence):
    elements = tokenize(sentence)
    parts = []
    for element in elements:
        parts.append(Token(classify(element), element))
    return parts
