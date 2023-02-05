class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def isBST(node):
    if node is None:
        return True

    # false if the max of the left is > than us
    if (node.left is not None and node.left > node.data):
        return False

    # false if the min of the right is <= than us
    if (node.right is not None and node.right < node.data):
        return False

    # false if, recursively, the left or right is not a BST
    if (isBST(node.left) is False or isBST(node.right) is False):
        return False

    # passing all that, it's a BST
    return True


def build_bst(lst):
    root = Node(lst[0])
    for i in range(1, len(lst)):
        insert(root, Node(lst[i]))
    return root

# Create the BST using the first list
bst = build_bst(["jaf","fjda","101","adfafs"])

# Insert the second list into the BST
for val in ["jaf","fjda","112","adfafs"]:
    insert(bst, Node(val))


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    # root.right.left = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)

    # Function call
    if isBST(root) is True:
        print("Is BST")
    else:
        print("Not a BST")