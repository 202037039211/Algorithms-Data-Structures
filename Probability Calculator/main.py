import copy
import random

class Hat:
    def __init__(self, **balls):
        # Initialize the Hat with a dictionary of balls, where keys are colors and values are counts
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # Draw balls from the hat without replacement
        if num_balls >= len(self.contents):
            # If more balls are requested than available, return all balls
            drawn_balls = self.contents[:]
            self.contents.clear()  # Clear the contents since all balls are drawn
            return drawn_balls
        else:
            # Draw without replacement, and remove each drawn ball from the contents
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls


# Test case 1: Drawing fewer balls than available
hat = Hat(blue=5, red=4, green=2)
drawn_balls = hat.draw(3)
print("Test 1 - Drawn Balls:", drawn_balls)
print("Test 1 - Remaining Contents:", hat.contents)

# Test case 2: Drawing more balls than available
drawn_balls = hat.draw(10)
print("Test 2 - Drawn Balls:", drawn_balls)
print("Test 2 - Remaining Contents after exceeding draw:", hat.contents)

# Resetting the hat for further testing
hat = Hat(red=2, blue=3)

# Test case 3: Draw exactly the number of balls available
drawn_balls = hat.draw(5)
print("Test 3 - Drawn Balls:", drawn_balls)
print("Test 3 - Remaining Contents:", hat.contents)  # Should be empty now

# Test case 4: Drawing 0 balls
drawn_balls = hat.draw(0)
print("Test 4 - Drawn Balls (0):", drawn_balls)
print("Test 4 - Remaining Contents (0):", hat.contents)  # Should still be empty
