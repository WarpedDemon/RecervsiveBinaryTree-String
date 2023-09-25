class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class TreeNode:
    def __init__(self, player):
        self.player = player
        self.left = None
        self.right = None

class PlayerBST:
    def __init__(self):
        self.root = None

    def insert(self, player):
        self.root = self._insert(self.root, player)

    def _insert(self, node, player):
        if node is None:
            return TreeNode(player)

        if player.name < node.player.name:
            node.left = self._insert(node.left, player)
        elif player.name > node.player.name:
            node.right = self._insert(node.right, player)
        else:
            # If a node with the same key exists, update its value
            node.player = player

        return node

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if node is None:
            return None
        if name == node.player.name:
            return node.player
        elif name < node.player.name:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    def print_tree(self):
        if not self.root:
            print("The tree is empty.")
            return

        def print_recursive(node, indent=""):
            if node is not None:
                print(indent + f"Name: {node.player.name}, Score: {node.player.score}")
                if node.left is not None or node.right is not None:
                    print(indent + "|")
                if node.left is not None:
                    print(indent + "+-- Left:")
                    print_recursive(node.left, indent + "|   ")
                if node.right is not None:
                    print(indent + "+-- Right:")
                    print_recursive(node.right, indent + "    ")

        print_recursive(self.root)

# Usage example:
bst = PlayerBST()
bst.insert(Player("Alice", 85))
bst.insert(Player("Bob", 92))
bst.insert(Player("Charlie", 78))
bst.insert(Player("David", 95))

print("Binary Search Tree:")
bst.print_tree()