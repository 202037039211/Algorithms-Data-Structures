# Probability Calculator

This project simulates a "hat" containing different colored balls and calculates the probability of drawing specific balls. The `Hat` class allows users to draw balls from the hat without replacement and handle different edge cases.

## Features:
- **Draw Balls**: Draw a specified number of balls from the hat.
- **Handle Edge Cases**: Handle cases where more balls are drawn than available or zero balls are drawn.
- **Clear Hat Contents**: Clear the hat after all balls are drawn.

## Class: `Hat`
- **Attributes**: 
  - `contents`: A list of balls in the hat, represented by color.
- **Methods**:
  - `draw(num_balls)`: Draws `num_balls` from the hat without replacement. If more balls are requested than available, it returns all the balls.
  
## Usage:
1. Create an instance of the `Hat` class by passing ball colors and counts as keyword arguments.
2. Use the `draw()` method to draw balls from the hat.

### Example:

```python
# Create a Hat with 5 blue, 4 red, and 2 green balls
hat = Hat(blue=5, red=4, green=2)

# Draw 3 balls
drawn_balls = hat.draw(3)
print(drawn_balls)  # Output: A list of 3 drawn balls

# Draw 10 balls (more than available)
drawn_balls = hat.draw(10)
print(drawn_balls)  # Output: All balls in the hat

# Create a Hat with 2 red and 3 blue balls
hat = Hat(red=2, blue=3)

# Draw exactly 5 balls (all available)
drawn_balls = hat.draw(5)
print(drawn_balls)  # Output: A list of 5 drawn balls

# Draw 0 balls
drawn_balls = hat.draw(0)
print(drawn_balls)  # Output: []
```

# Error Handling:
  - Drawing more balls than available: If more balls are requested than present in the hat, it returns all available balls.
  - Drawing 0 balls: If 0 balls are drawn, it returns an empty list and leaves the hat unchanged.
