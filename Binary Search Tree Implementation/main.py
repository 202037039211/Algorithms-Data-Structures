class TreeNode:
    def __init__(self, key):
        # Initialize a tree node with the given key and no children
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        # String representation of the node (for printing)
        return str(self.key)

class BinarySearchTree:
    def __init__(self):
        # Initialize an empty binary search tree
        self.root = None

    def _insert(self, node, key):
        # Helper method for recursive insertion
        if node is None:
            # Create a new TreeNode if the spot is empty
            return TreeNode(key)
        
        if key < node.key:
            # Insert in the left subtree if the key is smaller
            node.left = self._insert(node.left, key)
        elif key > node.key:
            # Insert in the right subtree if the key is larger
            node.right = self._insert(node.right, key)
        
        return node  # Return the (unchanged) node pointer

    def insert(self, key):
        # Public method to insert a key
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        # Helper method for recursive search
        if node is None or node.key == key:
            # Return the node if found or None if not found
            return node
        
        if key < node.key:
            # Search the left subtree
            return self._search(node.left, key)
        
        # Search the right subtree
        return self._search(node.right, key)
    
    def search(self, key):
        # Public method to search for a key
        return self._search(self.root, key)

    def _delete(self, node, key):
        # Helper method for recursive deletion
        if node is None:
            return node  # Key not found, return None
        
        if key < node.key:
            # Traverse left subtree
            node.left = self._delete(node.left, key)
        elif key > node.key:
            # Traverse right subtree
            node.right = self._delete(node.right, key) 
        else:
            # Node with the key found, handle 3 cases:
            # 1. Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left   
            
            # 2. Node with two children: Get the inorder successor (smallest in the right subtree)
            node.key = self._min_value(node.right)
            # Delete the inorder successor
            node.right = self._delete(node.right, node.key)   
        
        return node  # Return the (unchanged) node pointer

    def delete(self, key):
        # Public method to delete a key
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        # Find the minimum value node in a subtree
        while node.left is not None:
            node = node.left
        return node.key  # Return the minimum key

    def _inorder_traversal(self, node, result):
        # Helper method for recursive inorder traversal
        if node:
            # Visit left subtree, current node, then right subtree
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        # Public method to get an inorder traversal of the tree
        result = []
        self._inorder_traversal(self.root, result)
        return result

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    nodes = [50, 30, 20, 40, 70, 60, 80]

    for node in nodes:
        bst.insert(node)

    print('Search for 80:', bst.search(80))  # Should return the node containing 80
    print("Inorder traversal:", bst.inorder_traversal())  # Should print the tree in sorted order

    bst.delete(40)  # Delete node with key 40

    print("Search for 40:", bst.search(40))  # Should return None (node not found)
    print('Inorder traversal after deleting 40:', bst.inorder_traversal())  # Tree after deletion
