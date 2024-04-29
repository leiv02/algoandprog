def is_valid_row(grid, row, num):

    return num not in grid[row]


def is_valid_column(grid, col, num):

    for row in range(9):
        if grid[row][col] == num:
            return False
    return True


def is_valid_box(grid, row, col, num):

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def is_valid_move(grid, row, col, num):

    return is_valid_row(grid, row, num) and \
           is_valid_column(grid, col, num) and \
           is_valid_box(grid, row, col, num)


def find_empty_location(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return -1, -1 


def sudoku_solver(grid):

    row, col = find_empty_location(grid)
    if row == -1 and col == -1:
        return True 

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if sudoku_solver(grid):
                return True
            grid[row][col] = 0  

    return False


# Example usage:
if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if sudoku_solver(sudoku_grid):
        for row in sudoku_grid:
            print(row)
    else:
        print("No solution exists.")
