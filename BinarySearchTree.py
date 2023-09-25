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

    def insert(self, player, current=None):
        if not self.root:
            self.root = TreeNode(player)
            return

        if current is None:
            current = self.root

        if player.name < current.player.name:
            if current.left is None:
                current.left = TreeNode(player)
            else:
                self.insert(player, current.left)
        elif player.name > current.player.name:
            if current.right is None:
                current.right = TreeNode(player)
            else:
                self.insert(player, current.right)
        else:
            # If a node with the same key exists, update its value
            current.player = player

    def insert_player(self, name, score):
        player = Player(name, score)
        self.insert(player)

    def _search(self, name, current):
        if current is None:
            return None
        if name == current.player.name:
            return current.player
        elif name < current.player.name:
            return self._search(name, current.left)
        else:
            return self._search(name, current.right)

    def search(self, name):
        return self._search(name, self.root)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.inorder_traversal(node.left)
            print(f"Name: {node.player.name}, Score: {node.player.score}")
            self.inorder_traversal(node.right)

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
bst.insert_player("Alice", 85)
bst.insert_player("Bob", 92)
bst.insert_player("Charlie", 78)
bst.insert_player("David", 95)

#print("Inorder traversal of the BST:")
#bst.inorder_traversal()

# Search for a player
# search_name = "Bob"
# found_player = bst.search(search_name)
# if found_player:
#    print(f"Found {search_name}: Score - {found_player.score}")
# else:
#    print(f"{search_name} not found in the BST.")

print("Binary Search Tree:")
bst.print_tree()