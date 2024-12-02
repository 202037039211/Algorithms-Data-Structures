class Rectangle:
    def __init__(self, width, height):
        # Initialize the width and height of the rectangle
        self.width = width
        self.height = height

    def set_width(self, width):
        # Set the width of the rectangle
        self.width = width

    def set_height(self, height):
        # Set the height of the rectangle
        self.height = height

    def get_area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height

    def get_perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        # Calculate and return the diagonal length of the rectangle
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Generate a visual representation of the rectangle using asterisks
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ("*" * self.width + "\n") * self.height
        return picture

    def get_amount_inside(self, shape):
        # Calculate how many times the provided shape can fit inside the rectangle
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        # String representation of the rectangle object
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Initialize a square by setting both width and height to the same value
        super().__init__(side, side)

    def set_side(self, side):
        # Set both width and height to the same value to define a square
        self.width = side
        self.height = side

    def set_width(self, width):
        # Set the width and adjust height to maintain square properties
        self.set_side(width)

    def set_height(self, height):
        # Set the height and adjust width to maintain square properties
        self.set_side(height)

    def __str__(self):
        # String representation of the square object
        return f"Square(side={self.width})"


# Test cases
rect = Rectangle(10, 5)
print(rect.get_area())          # Expected output: 50
rect.set_height(3)
print(rect.get_perimeter())     # Expected output: 26
print(rect)                     # Expected output: Rectangle(width=10, height=3)
print(rect.get_picture())       # Expected output: Picture of rectangle

sq = Square(9)
print(sq.get_area())            # Expected output: 81
sq.set_side(4)
print(sq.get_diagonal())        # Expected output: 5.656854249492381
print(sq)                       # Expected output: Square(side=4)
print(sq.get_picture())         # Expected output: Picture of square

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Expected output: 8
