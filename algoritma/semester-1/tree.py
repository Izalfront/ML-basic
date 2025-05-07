class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# Fungsi untuk menampilkan tree secara visual (dalam bentuk teks)
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Buat node
akar = TreeNode(9)
anak_kiri = TreeNode(3)
anak_kanan = TreeNode(8)

# Sambungkan node
akar.left = anak_kiri
akar.right = anak_kanan

# Cetak visualisasi tree
print_tree(akar)
