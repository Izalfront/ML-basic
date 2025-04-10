class Solution(object):
    def romanToInt(self, s):
        # buat huruf ini punya value sendiri yang akan nanti dijumlahkan
        # jumlahkan huruf beruntun sesuai inputan user
        # tampilkan hasil
        symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and symbol_value[s[i]] < symbol_value[s[i + 1]]:
                res -= symbol_value[s[i]]
            else:
                res += symbol_value[s[i]]
        return res
            
            