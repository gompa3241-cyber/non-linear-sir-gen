
from collections import deque, defaultdict


# --- 1. BINARY TREE IMPLEMENTATION ---
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_bfs(root):
    if not root:
        return []

    queue = deque([root])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Tree BFS:", " -> ".join(order))


def tree_dfs_preorder(root, order=None):
    if order is None:
        order = []

    if root:
        order.append(root.val)
        tree_dfs_preorder(root.left, order)
        tree_dfs_preorder(root.right, order)

    return order


# --- 2. GRAPH IMPLEMENTATION (ADJACENCY LIST) ---
class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("Graph BFS:", " -> ".join(order))

    def dfs(self, start):
        visited = set()
        order = []
        self._dfs_helper(start, visited, order)
        print("Graph DFS:", " -> ".join(order))

    def _dfs_helper(self, current, visited, order):
        visited.add(current)
        order.append(current)

        for neighbor in self.adj_list[current]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, order)


if __name__ == "__main__":
    print("=== ASSESSMENT 3.4: NON-LINEAR DATA STRUCTURES (ABELLA) ===")

    # Building Tree for ABELLA (Unique Letters)
    # Level 0 (Root): A
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('E')
    root.left.left = TreeNode('L')

    print("\n--- Binary Tree Traversals ---")
    tree_bfs(root)

    tree_dfs_order = tree_dfs_preorder(root)
    print("Tree DFS (Pre-order):", " -> ".join(tree_dfs_order))

    # Building Graph for ABELLA (Unique Letters)
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'L')
    graph.add_edge('B', 'E')
    graph.add_edge('E', 'L')

    print("\n--- Graph Traversals (Starting from A) ---")
    graph.bfs('A')
    graph.dfs('A')
