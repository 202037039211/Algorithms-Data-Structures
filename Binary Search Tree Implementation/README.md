# Binary Search Tree Implementation in Python

This project implements a Binary Search Tree (BST) in Python, featuring standard operations such as insertion, search, deletion, and traversal.

## Features:
- **Insertion**: Add nodes to the BST.
- **Search**: Find nodes within the BST.
- **Deletion**: Remove nodes while maintaining BST properties.
- **Inorder Traversal**: Traverse the tree in sorted order.

## Usage:
1. Create a `BinarySearchTree` object.
2. Use `insert()` to add elements.
3. Use `search()` to check for elements.
4. Use `delete()` to remove elements.
5. Use `inorder_traversal()` to view elements in sorted order.

## Example:
```python
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
print(bst.inorder_traversal())  # Output: [30, 50, 70]
```
