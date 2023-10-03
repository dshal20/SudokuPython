import pygame
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty, sudoku_board):
        self.width = width
        self.height = height - 100
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_row = None
        self.selected_col = None
        self.original_board = sudoku_board
        self.current_board = sudoku_board


    def draw(self):

        self.screen.fill((255, 255, 255))

        # Draw the Sudoku grid
        for i in range(10):
            if i % 3 == 0:
                line_width = 3

            else:
                line_width = 1

            pygame.draw.line(self.screen, (0, 0, 0), (i * self.width / 9, 0), (i * self.width / 9, self.height), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.height / 9), (self.width, i * self.height / 9), line_width)

        # Draw each cell
        for index, row in enumerate(self.current_board):
            for col, value2 in enumerate(self.current_board[index]):
                self.cells[index][col].set_cell_value(value2)
                self.cells[index][col].draw()



    def select(self, row, col): # Mark the cell at (row, col) as the current selected cell

        if self.selected_row is not None and self.selected_col is not None:
            self.cells[self.selected_row][self.selected_col].selected = False

        self.selected_row = row
        self.selected_col = col
        self.cells[row][col].selected = True



    def click(self, x, y): # Return the (row, col) of the cell that was clicked

        if x < 0 or y < 0 or x > self.width or y > self.height:
            return None

        row = int(y // (self.height / 9))
        col = int(x // (self.width / 9))
        return (row, col)



    def clear(self): # Clear the value of the selected cell

        if self.selected_row is not None and self.selected_col is not None and self.original_board[self.selected_row][self.selected_col] == 0:
            self.cells[self.selected_row][self.selected_col].set_cell_value(0)


    def sketch(self, value): # Set the sketched value of the selected cell

        if self.selected_row is not None and self.selected_col is not None and self.cells[self.selected_row][self.selected_col].value == 0:
            self.cells[self.selected_row][self.selected_col].set_sketched_value(value)


    def place_number(self, value): # Set the value of the cell

        if self.selected_row is not None and self.selected_col is not None and self.cells[self.selected_row][self.selected_col].value == 0:
            self.cells[self.selected_row][self.selected_col].set_cell_value(value)



    def reset_to_original(self): # reset all cells to the original values

        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.original_board[i][j])
                self.cells[i][j].set_sketched_value((None))

    def is_full(self): # Check if board is full

        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True



    def update_board(self): # Update the underlying 2D board with the values in all cells

        self.current_board = [[self.cells[row][col].value for col in range(9)] for row in range(9)]

    def find_empty(self): # Find an empty cell and return its (row, col)

        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return (row, col)
        return None



    def check_board(self):
        # Check rows
        for row in range(9):
            nums = set()
            for col in range(9):
                cell = self.cells[row][col]
                if cell.value != 0:
                    if cell.value in nums:
                        return False
                    nums.add(cell.value)

        # Check columns
        for col in range(9):
            nums = set()
            for row in range(9):
                cell = self.cells[row][col]

                if cell.value != 0:
                    if cell.value in nums:
                        return False

                    nums.add(cell.value)

        # Check squares
        for i in range(3):
            for j in range(3):
                nums = set()
                for row in range(3 * i, 3 * i + 3):
                    for col in range(3 * j, 3 * j + 3):
                        cell = self.cells[row][col]
                        if cell.value != 0:
                            if cell.value in nums:
                                return False
                            nums.add(cell.value)

        # If all checks passed, the board is solved correctly
        return True