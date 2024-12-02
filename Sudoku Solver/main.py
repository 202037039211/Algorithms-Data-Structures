class Board:
    def __init__(self, board):
        # Initialize the Sudoku board
        self.board = board

    def __str__(self):
        # Generate a human-readable string representation of the board
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]  # Replace 0s with '*' for display
            board_str += ' '.join(row_str) + '\n'
        return board_str

    def find_empty_cell(self):
        # Find the next empty cell (represented by 0)
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col  # Return the coordinates of the empty cell
            except ValueError:
                continue  # Move to the next row if no empty cell is found
        return None  # No empty cell found; board is full

    def valid_in_row(self, row, num):
        # Check if the number is not already in the specified row
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Check if the number is not already in the specified column
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # Check if the number is not already in the 3x3 square containing the cell
        row_start = (row // 3) * 3  # Starting row index of the square
        col_start = (col // 3) * 3  # Starting column index of the square
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # Check if placing the number in the empty cell is valid
        row, col = empty
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_square(row, col, num))

    def solver(self):
        # Recursively solve the Sudoku puzzle using backtracking
        next_empty = self.find_empty_cell()
        if next_empty is None:
            return True  # Puzzle is solved if no empty cells are left
        
        row, col = next_empty
        for guess in range(1, 10):  # Try all numbers from 1 to 9
            if self.is_valid((row, col), guess):
                self.board[row][col] = guess  # Place the number if it's valid
                
                if self.solver():
                    return True  # Continue with the next empty cell
                
                self.board[row][col] = 0  # Backtrack if placing the number didn't lead to a solution
        return False  # No solution found

def solve_sudoku(board):
    # Create a Board object and solve the Sudoku puzzle
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

# Example puzzle to solve
puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)
