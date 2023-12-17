import nltk
from nltk.tokenize import sent_tokenize

kalimat = "Pengembangan layanan kesehatan dinilai dapat mempercepat proses transformasi digital kesehatan di Indonesia. Untuk itu, pemanfaatan teknologi dibutuhkan agar dapat mempermudah akses layanan kesehatan yang dapat dijangkau oleh masyarakat."

tokens = nltk.tokenize.sent_tokenize(kalimat)
print(tokens)