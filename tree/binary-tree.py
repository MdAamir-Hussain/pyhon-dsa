class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, current_node, traversal):
        if current_node is not None:
            traversal = self._inorder_traversal(current_node.left, traversal)
            traversal.append(current_node.key)
            traversal = self._inorder_traversal(current_node.right, traversal)
        return traversal

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, current_node, traversal):
        if current_node is not None:
            traversal.append(current_node.key)
            traversal = self._preorder_traversal(current_node.left, traversal)
            traversal = self._preorder_traversal(current_node.right, traversal)
        return traversal

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, current_node, traversal):
        if current_node is not None:
            traversal = self._postorder_traversal(current_node.left, traversal)
            traversal = self._postorder_traversal(current_node.right, traversal)
            traversal.append(current_node.key)
        return traversal

# Example of creating and using the binary tree
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

print("Inorder traversal:", tree.inorder_traversal())
print("Preorder traversal:", tree.preorder_traversal())
print("Postorder traversal:", tree.postorder_traversal())
