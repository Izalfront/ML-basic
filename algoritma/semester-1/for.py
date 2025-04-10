class Solution(object):
    def deleteDuplicates(head):
        head = [1,2,2]
        angka_unik = []
        for index in head:
            if index not in angka_unik:
                angka_unik.append(index)

        hasil = sorted(angka_unik, reverse=False)
        print(hasil)