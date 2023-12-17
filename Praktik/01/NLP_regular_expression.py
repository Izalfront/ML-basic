import re # import modul regular expression

kalimat = "Solusi Vision Intelligence (VI) Coconut Counter diciptakan Widya Robotics untuk menghitung jumlah kelapa yang melewati conveyor sehingga bisa meningkatkan kapasitas produksi sampai tiga kali lipat, kata Head of AI Division Widya Robotics Ruby Abdullah dalam siaran pers, Jumat (18/3/2022)."

hasil = re.sub(r"\d+", "", kalimat)
print(hasil)