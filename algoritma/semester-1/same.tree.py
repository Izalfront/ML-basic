def isSameTree(p, q):
    # Kalau dua-duanya kosong, berarti sama
    if not p and not q:
        return True
    
    # Kalau salah satu kosong, atau nilainya beda → tidak sama
    if not p or not q or p.val != q.val:
        return False

    # Cek anak kiri dan anak kanan
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
