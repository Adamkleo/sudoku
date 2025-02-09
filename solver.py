from grid import SudokuGrid

class SudokuSolver:
    def __init__(self, grid: SudokuGrid):
        self.grid = grid

    def is_valid(self, row, col, num):
        return (
            num not in self.grid.get_row(row) and
            num not in self.grid.get_column(col) and
            num not in self.grid.get_block(row, col)
        )
    
    def solve(self):
        raise NotImplementedError