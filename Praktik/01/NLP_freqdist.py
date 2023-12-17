import nltk
import matplotlib.pyplot as plt

nltk.download('punkt')

from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize

text="Nama saya Muhammad Rizal Wahyudi Lahir di kandangan Pendidikan SMA saya di ....."\
    "Sekarang menjadi mahasiswa Politeknik Negeri Banjarmasin Jurusan Teknik Elektro."\
    "Hobby saya adalah Design UI/UX"

tokenize = nltk.tokenize.word_tokenize(text)
FreqDist = nltk.FreqDist(tokenize)
print(FreqDist.most_common())

FreqDist.plot(30,cumulative=False)
plt.show()