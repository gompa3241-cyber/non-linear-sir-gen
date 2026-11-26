from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs_preorder(root, order=None):
    """Root -> Left -> Right"""
    if order is None:
        order = []
    if root:
        order.append(root.val)
        dfs_preorder(root.left, order)
        dfs_preorder(root.right, order)
    return order


def dfs_inorder(root, order=None):
    """Left -> Root -> Right"""
    if order is None:
        order = []
    if root:
        dfs_inorder(root.left, order)
        order.append(root.val)
        dfs_inorder(root.right, order)
    return order


def dfs_postorder(root, order=None):
    """Left -> Right -> Root"""
    if order is None:
        order = []
    if root:
        dfs_postorder(root.left, order)
        dfs_postorder(root.right, order)
        order.append(root.val)
    return order


def build_tree_level_order(values):
    """Builds a binary tree level-by-level from a list of node values."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        if index < len(values):
            current.left = TreeNode(values[index])
            queue.append(current.left)
            index += 1

        if index < len(values):
            current.right = TreeNode(values[index])
            queue.append(current.right)
            index += 1

    return root


if __name__ == "__main__":
    print("=== ASSESSMENT 3.6: DFS METHODS IN TREE (CRISTIAN ABELLA) ===")

    # First Name + Last Name letters: C R I S T I A N A B E L L A
    letters = list("CRISTIANABELLA")
    root = build_tree_level_order(letters)

    preorder_result = dfs_preorder(root)
    inorder_result = dfs_inorder(root)
    postorder_result = dfs_postorder(root)

    print("\nPreOrder  (Root -> Left -> Right): ", " -> ".join(preorder_result))
    print("InOrder   (Left -> Root -> Right): ", " -> ".join(inorder_result))
    print("PostOrder (Left -> Right -> Root): ", " -> ".join(postorder_result))