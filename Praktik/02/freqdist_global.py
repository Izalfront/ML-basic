import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

fdist = FreqDist()

def hitung_kata(text):
    tokenized_word = word_tokenize(text)
    global fdist
    fdist.update(tokenized_word)

text1 = "Apel adalah buah yang enak, dan apel sangat sehat untuk tubuh."
hitung_kata(text1)

text2 = "Semangka adalah buah musim panas yang segar dan enak."
hitung_kata(text2)

print(fdist.most_common())
