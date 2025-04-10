# I II III IV V VI VII VIII IX X
#  symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#  tetntukan jumlah array per karakter, misa XII berarti ada 3 array
#  jika array (0) lebih kecil daripada array (0+1) maka (0+1) - (0)
#  jika array (0) lebih besar daripada array (0+1) maka (0) + (0+1)
#  lakukan pengulangan hingga array terakhir
#  tampilkan hasil 
def int_to_roman(s: int) -> str:
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    while s > 0:
        for i in range(len(val)):
            if s >= val[i]:
                roman += sym[i]
                s -= val[i]
            i+= 1
        return roman

# Contoh penggunaan
print(int_to_roman(1994)) 

class Solution(object):
    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        
        for char in reversed(s): 
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total


# #  symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#  tetntukan jumlah array per karakter, misa XII berarti ada 3 array
#  1555 = 1000 + 500 + 50 + 5 MDLV
# jika angka <= 3 maka tetap = III
# jika angka == 4 && ankga > 3 && angka <= 5 maka = V=5 - I=1 = IV
# jika angka == 5 maka = angka romawi baru = V, L, C  