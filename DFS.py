from stack import Stack
from solver import SudokuSolver

class BacktrackingSolver(SudokuSolver):
    def solve(self):
        s = Stack()
        grid = self.grid.cells
        index = 0
        last_num = 1
        solution_found = True

        empty_positions = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]

        while index < len(empty_positions):
            i, j = empty_positions[index]
            placed = False

            for num in range(last_num, 10):
                if self.is_valid(i, j, num):
                    s.push((index, num))
                    grid[i][j] = num
                    index += 1
                    placed = True
                    last_num = 1
                    break

            if not placed:
                if s.is_empty():
                    solution_found = False
                    break

                last_index, last_num = s.pop()
                i, j = empty_positions[last_index]
                grid[i][j] = 0
                index = last_index
                last_num += 1

        if not solution_found:
            print("No solution found!")
            return -1

        return 0
