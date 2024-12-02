NUMBER_OF_DISKS = 5  # Total number of disks

# Initialize the towers: A has all the disks initially, B and C are empty
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    
    # Move n - 1 disks from the source to the auxiliary (temporary) tower
    move(n - 1, source, target, auxiliary)
    
    # Move the nth (largest) disk directly from the source to the target
    target.append(source.pop())
    
    # Display the current state of all three towers after each move
    print(A, B, C, '\n')
    
    # Move the n - 1 disks from the auxiliary tower to the target
    move(n - 1, auxiliary, source, target)
    
# Start the recursive process from tower A to tower C, using tower B as auxiliary
move(NUMBER_OF_DISKS, A, B, C)
