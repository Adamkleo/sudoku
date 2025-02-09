from solver import SudokuSolver
from constraint import Problem, AllDifferentConstraint


class CSPSolver(SudokuSolver):
    def solve(self):
        problem = Problem()

        self.addVariables(problem)
        self.addRowConstraint(problem)
        self.addColumnConstraint(problem)
        self.addBlockConstraint(problem)

        def solution_to_matrix(solution, original_grid):
            matrix = [row[:] for row in original_grid]  # Copy the original grid

            for (row, col), value in solution.items():
                matrix[row][col] = value  # Assign CSP values

            return matrix

        # Solve and display some solutions
        solution = problem.getSolution()
        if solution:
            self.grid.cells = solution_to_matrix(solution, self.grid.cells)
            return 0
        else:
            print("No solution found!")
            return -1
            


    def addVariables(self, problem):
        for i in range(len(self.grid.cells)):
            for j in range(len(self.grid.cells[i])):
                if self.grid.cells[i][j] == 0:
                    problem.addVariable((i, j), range(1,10))


    def addRowConstraint(self, problem):
        for i in range(9):  # Iterate through each row
            empty_positions = []
            existing_values = set()

            for j in range(9):  # Iterate through columns in the row
                if self.grid.cells[i][j] == 0:
                    empty_positions.append((i, j))  # Store variable positions
                else:
                    existing_values.add(self.grid.cells[i][j])  # Store fixed values

            if empty_positions:
                # Ensure all empty positions in the row have unique values
                problem.addConstraint(AllDifferentConstraint(), empty_positions)

                # Ensure none of the empty positions take a value already in the ro
                for pos in empty_positions:
                    problem.addConstraint(lambda x, fixed=existing_values: x not in fixed, [pos])


    def addColumnConstraint(self, problem):
        for i in range(9):  
            empty_positions = []
            existing_values = set()

            for j in range(9): 
                if self.grid.cells[j][i] == 0:
                    empty_positions.append((j, i)) 
                else:
                    existing_values.add(self.grid.cells[j][i])  

            if empty_positions:
            
                problem.addConstraint(AllDifferentConstraint(), empty_positions)
                
                for pos in empty_positions:
                    problem.addConstraint(lambda x, fixed=existing_values: x not in fixed, [pos])

    def addBlockConstraint(self, problem):

        for block_i in range(3):  
            for block_j in range(3): 
                empty_positions = []
                existing_values = set()

                
                for i in range(3):
                    for j in range(3):
                        row = block_i * 3 + i
                        col = block_j * 3 + j

                        if self.grid.cells[row][col] == 0:
                            empty_positions.append((row, col)) 
                        else:
                            existing_values.add(self.grid.cells[row][col])

                if empty_positions:
                    
                    problem.addConstraint(AllDifferentConstraint(), empty_positions)

                    
                    for pos in empty_positions:
                        problem.addConstraint(lambda x, fixed=existing_values: x not in fixed, [pos])



