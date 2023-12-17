import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

kata = ["study","studying","studies","student","students","leon","leons"]

for k in kata:
    print(k, " : ", ps.stem(k))