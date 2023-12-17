import speech_recognition as sr

engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""
engine.pause_treshold = 3

with mic as source:
    print("Silahkan mulai bicara")
    rekaman = engine.listen(source)
    print("waktu habis")

    try:
        hasil = engine.recognize_google(rekaman, language = "id-ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Maaf suara anda tidak terdeteksi, coba lagi")
    except Exception as e:
        print(e)

text_file = open("Hasil.txt", "w")
text_file.write(hasil)
text_file.close()