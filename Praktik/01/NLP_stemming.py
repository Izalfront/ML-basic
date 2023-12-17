# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stemming process
sentence = 'Dengan adanya solusi Vision Intelligence, pekerjaan yang dulu tergantung pada kejelian mata dapat digantikan dengan kecerdasan buatan.'
output = stemmer.stem(sentence)
print (output)

print(stemmer.stem('Teknologi AI dapat meniru-nirukan perilaku dan memudahkan aktivitas manusia.'))
