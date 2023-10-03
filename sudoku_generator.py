import math, random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = self.generate_board()
        self.box_length = int(math.sqrt(self.row_length))

    def generate_board(self):
        self.board = []
        for i in range(self.row_length):
            self.board.append([])
            for j in range(self.row_length):
                self.board[i].append(0)
        return self.board

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(self.row_length):
            counter = 0
            for j in range(self.row_length):
                print(self.board[i][j], end='  ')
                counter += 1
                if counter == 9:
                    print()

    def valid_in_row(self, row, num):
        row, num = int(row), int(num)
        for i in self.board[row]:
            if i == num:
                return False
        return True

    def valid_in_col(self, col, num):
        col, num = int(col), int(num)
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        col_start, row_start, num = int(col_start), int(row_start), int(num)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if num == self.board[i][j]:
                    return False
        return True

    def is_valid(self, row, col, num):
        row, col, num = int(row), int(col), int(num)
        if row in range(3):
            if col in range(3):
                row_start = 0
                col_start = 0
            elif col in range(3, 6):
                row_start = 0
                col_start = 3
            elif col in range(6, 9):
                row_start = 0
                col_start = 6
        elif row in range(3, 6):
            if col in range(3):
                row_start = 3
                col_start = 0
            elif col in range(3, 6):
                row_start = 3
                col_start = 3
            elif col in range(6, 9):
                row_start = 3
                col_start = 6
        elif row in range(6, 9):
            if col in range(3):
                row_start = 6
                col_start = 0
            elif col in range(3, 6):
                row_start = 6
                col_start = 3
            elif col in range(6, 9):
                row_start = 6
                col_start = 6
        if self.valid_in_col(col, num) and self.valid_in_row(row, num) and self.valid_in_box(row_start, col_start, num):
            return True
        return False

    def fill_box(self, row_start, col_start):
        number_list = []
        row_start, col_start = int(row_start), int(col_start)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                random_number = random.randint(1, 9)
                while True:
                    if random_number not in number_list:
                        self.board[i][j] = random_number
                        break
                    else:
                        random_number = random.randint(1, 9)
                number_list.append(random_number)

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            row, col = int(row), int(col)
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        for i in range(self.removed_cells):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while True:
                if self.board[row][col] == 0:
                    row = random.randint(0, 8)
                    col = random.randint(0, 8)
                else:
                    break
            self.board[row][col] = 0

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board