import string

kalimat = "Apakah k@limat ini & merupakan [contoh] kalimat ? {dengan} tanda, baca?!!"
hasil = kalimat.translate(str.maketrans("","",string.punctuation))
print(hasil)