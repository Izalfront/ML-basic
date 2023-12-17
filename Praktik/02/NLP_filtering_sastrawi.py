import nltk
import string

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from nltk.tokenize import word_tokenize

stop_factory = StopWordRemoverFactory().get_stop_words() #load default stopword
more_stopword = ['daring','online'] #menambahkan stopword = mengurangi jumlah kata
kalimat = "Mangde kerap melakukan transaksi rutin secara daring atau online. Menurut Majidi belanja online lebih praktis"
kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()
data = stop_factory + more_stopword #menggabungkan stopword

dictionary = ArrayDictionary(data)
str = StopWordRemover(dictionary)
tokens = nltk.tokenize.word_tokenize(str.remove(kalimat))
print(tokens)
