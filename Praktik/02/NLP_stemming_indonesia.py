import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

kalimat = "Mangde kerap melakukan transaksi rutin secara daring atau online"
hasil = stemmer.stem(kalimat)
print(hasil)