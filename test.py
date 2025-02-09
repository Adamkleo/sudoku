import copy
import time
from grid import SudokuGrid
from DFS import BacktrackingSolver
from CSP import CSPSolver

values = [
    5, 3, 0, 0, 7, 0, 0, 0, 0,
    6, 0, 0, 1, 9, 5, 0, 0, 0,
    0, 9, 8, 0, 0, 0, 0, 6, 0,
    8, 0, 0, 0, 6, 0, 0, 0, 3,
    4, 0, 0, 8, 0, 3, 0, 0, 1,
    7, 0, 0, 0, 2, 0, 0, 0, 6,
    0, 6, 0, 0, 0, 0, 2, 8, 0,
    0, 0, 0, 4, 1, 9, 0, 0, 5,
    0, 0, 0, 0, 8, 0, 0, 7, 9
]

# Create independent copies of the grid
grids = [SudokuGrid(copy.deepcopy(values)) for _ in range(2)]
solvers = [BacktrackingSolver(grids[0]), CSPSolver(grids[1])]
solver_names = ["Backtracking Solver", "CSP Solver"]

# Print the initial grid
print("Initial Grid:")
grids[0].print_grid()
print("")

# Run each solver and measure execution time
for i, solver in enumerate(solvers):
    print(f"Solving with {solver_names[i]}...")
    start_time = time.time()
    solver.solve()
    end_time = time.time()
    
    print(f"{solver_names[i]} took {end_time - start_time:.6f} seconds.")
    grids[i].print_grid()
    print("")
