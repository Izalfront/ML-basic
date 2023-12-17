import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize

text="Di kelas TI -4Axioo sedang belajar pemrograman Natural Language Processing menggunakan Bahasa Python."

tokenized_text =sent_tokenize(text)
print (tokenized_text)