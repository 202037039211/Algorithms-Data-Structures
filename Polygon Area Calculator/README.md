# Polygon Area Calculator

This project calculates the area, perimeter, diagonal, and other properties of rectangular and square shapes. It also supports visualizing these shapes as text and calculating how many smaller shapes fit inside a larger one.

## Features:
- **Calculate Area**: Calculate the area of rectangles and squares.
- **Calculate Perimeter**: Calculate the perimeter of rectangles.
- **Calculate Diagonal**: Calculate the diagonal of squares and rectangles.
- **Visualize Shapes**: Generate a text-based visual representation of shapes.
- **Shape Fitting**: Calculate how many smaller shapes can fit inside a larger shape.

## Classes:
- **Rectangle**: The base class to represent rectangular shapes.
- **Square**: A subclass of Rectangle that enforces equal width and height.

## Usage:
1. Create a rectangle or square by instantiating the respective class.
2. Use the provided methods to calculate area, perimeter, diagonal, and more.

### Example:

```python
# Create a Rectangle
rect = Rectangle(10, 5)
print(rect.get_area())  # Output: 50
print(rect.get_perimeter())  # Output: 26
print(rect.get_picture())  # Visual representation

# Create a Square
sq = Square(9)
print(sq.get_area())  # Output: 81
print(sq.get_diagonal())  # Output: 5.656854249492381
```

# Error Handling:
  - Rectangle too big for picture: If either the width or height exceeds 50, the picture cannot be displayed. Error: Too big for picture.
