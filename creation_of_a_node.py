"""Binary tree and binary search tree (BST) basics.

Sections:
    1. Node
    2. General binary tree: traversals and metrics
    3. Binary search tree: search, insert, delete
    4. Demo (main)
"""


# --------------------------------------------------------------------------
# 1. Node
# --------------------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# --------------------------------------------------------------------------
# 2. General binary tree: traversals and metrics
# --------------------------------------------------------------------------

def preorder(node):
    """Root, left, right. Returns a list of values."""
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def inorder(node):
    """Left, root, right. Returns a list of values."""
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def postorder(node):
    """Left, right, root. Returns a list of values."""
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def height(node):
    """Edges on the longest root-to-leaf path. Empty tree is -1."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


# --------------------------------------------------------------------------
# 3. Binary search tree
# --------------------------------------------------------------------------

def bst_search(node, target):
    if node is None:
        return False
    if target == node.value:
        return True
    if target < node.value:
        return bst_search(node.left, target)
    return bst_search(node.right, target)


def insert(root, value):
    """Insert value and return the (possibly new) root. Duplicates are ignored."""
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def min_value_node(node):
    """Leftmost node of a subtree, which holds its smallest value."""
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete(root, value):
    """Delete value if present and return the (possibly new) root."""
    if root is None:
        return None

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        # Found the node. Handle 0 or 1 child first.
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Two children: replace with the inorder successor, then delete it.
        successor = min_value_node(root.right)
        root.value = successor.value
        root.right = delete(root.right, successor.value)

    return root


def build_bst(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


# --------------------------------------------------------------------------
# 4. Demo
# --------------------------------------------------------------------------

def build_sample_tree():
    """
          1
         / \\
        2   3
       / \\
      4   5
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def show(label, values):
    print(f"{label:<10}: {' '.join(str(v) for v in values)}")


def demo_binary_tree():
    print("=== Binary tree ===")
    root = build_sample_tree()

    show("Preorder", preorder(root))
    show("Inorder", inorder(root))
    show("Postorder", postorder(root))

    print(f"Nodes     : {count_nodes(root)}")
    print(f"Leaves    : {count_leaves(root)}")
    print(f"Height    : {height(root)}")


def demo_bst():
    print("\n=== Binary search tree ===")
    root = build_bst([50, 30, 70, 20, 40, 60, 80])
    show("Inorder", inorder(root))

    for target in (60, 65):
        print(f"Search {target}: {bst_search(root, target)}")

    for value in (20, 30, 50):  # leaf, one child, two children (root)
        root = delete(root, value)
        show(f"Del {value}", inorder(root))


def main():
    demo_binary_tree()
    demo_bst()


if __name__ == "__main__":
    main()