class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(t, True)
        self.t = t

    def search(self, k, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and x.keys[i] == k:
                return (x, i)
            else:
                return None
        elif i < len(x.keys) and k == x.keys[i]:
            return self.search(k, x.children[i + 1])
        else:
            return self.search(k, x.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            s = BPlusTreeNode(self.t, False)
            self.root = s
            s.children.insert(0, root)
            self.split_child(s, 0)
            self.insert_non_full(s, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BPlusTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t - 1:]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t - 1:]
            y.children = y.children[0: t - 1]
        if y.leaf:
            z.next = y.next
            y.next = z

# Example of creating and using a B+ tree
bplustree = BPlusTree(3)  # A B+ tree with minimum degree 3
for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    bplustree.insert(key)

print("Search for key 6 in B+ tree:", bplustree.search(6))
print("Search for key 15 in B+ tree:", bplustree.search(15))
