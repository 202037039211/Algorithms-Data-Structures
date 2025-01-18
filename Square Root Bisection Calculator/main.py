def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Calculate the square root of a number using the bisection method.

    Parameters:
    - square_target (float): The number to find the square root of.
    - tolerance (float): The precision of the result.
    - max_iterations (int): The maximum number of iterations to prevent infinite loops.

    Returns:
    - root (float): The approximate square root.
    """
    # Check for invalid (negative) inputs
    if square_target < 0:
        raise ValueError('Square root of a negative number is not defined in real numbers.')
    
    # Handle special cases for 0 and 1
    if square_target == 0:
        print(f'The square root of {square_target} is 0.')
        return 0
    if square_target == 1:
        print(f'The square root of {square_target} is 1.')
        return 1

    # Set the initial range for the bisection search
    low = 0
    high = max(1, square_target)  # Ensures the range is valid even for numbers between 0 and 1
    root = None

    # Perform the bisection method
    for _ in range(max_iterations):
        mid = (low + high) / 2  # Midpoint of the current range
        square_mid = mid**2  # Calculate the square of the midpoint

        # Check if the current approximation is within the tolerance
        if abs(square_mid - square_target) < tolerance:
            root = mid
            break

        # Adjust the search range based on the current midpoint's square value
        if square_mid < square_target:
            low = mid
        else:
            high = mid

    # Provide feedback if the algorithm did not converge
    if root is None:
        print(f"Failed to converge within {max_iterations} iterations.")
        return None
    
    # Print and return the calculated square root
    print(f'The square root of {square_target} is approximately {root:.7f}')
    return root

# Example usage
if __name__ == "__main__":
    N = 16  # Change this value to test different numbers
    square_root_bisection(N)
