import nltk

separator_tags = ['CC', 'IN', 'MD', 'TO', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP']
verb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
adjective_tags = ['JJ', 'JJR', 'JJS']
noun_tags = ['NN', 'NNP']

reminders = ['remember', 'remind']
times = ['tomorrow', 'today', 'noon', 'midnight']
priorities = ['low', 'medium', 'high']


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


def tokenize_and_tag(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged


def tokenize(sentence):
    tagged_words = tokenize_and_tag(sentence)
    elements = []
    curr = []
    for tagged in tagged_words:
        if tagged[1] in separator_tags or tagged[0] in priorities or tagged[0] == 'due' or tagged[0] in times:
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
