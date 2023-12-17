import re
import random

sapaan = ["hai juga","ok","Halo Juga"]

while True:
    x = input("User\t: ")
    
    if re.findall(r"halo|hai", x):
        print("Bot\t:", random.choice(sapaan))
    else:
        print("Bot\t: Aku tidak paham")