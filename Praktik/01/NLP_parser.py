import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "I shot an elephant in my pajamas"
tokenized_word=word_tokenize(text)
print(tokenized_word)

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(tokenized_word):
    print(tree)
    tree.draw()