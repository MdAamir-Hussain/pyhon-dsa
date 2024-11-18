class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node
        self.keys = []  # List of keys
        self.children = []  # List of child pointers

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t  # Minimum degree

    def traverse(self, x=None):
        if x is None:
            x = self.root
        for i in range(len(x.keys)):
            if not x.leaf:
                self.traverse(x.children[i])
            print(x.keys[i], end=" ")
        if not x.leaf:
            self.traverse(x.children[len(x.keys)])

    def search(self, k, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return self.search(k, x.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            s = BTreeNode(self.t, False)
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
        z = BTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t]

# Example of creating and using a B-tree
btree = BTree(3)  # A B-tree with minimum degree 3
for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    btree.insert(key)

print("Traversal of B-tree:")
btree.traverse()
print("\nSearch for key 6 in B-tree:", btree.search(6))
print("Search for key 15 in B-tree:", btree.search(15))
