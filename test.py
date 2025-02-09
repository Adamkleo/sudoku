import time
from grid import SudokuGrid
from DFS import BacktrackingSolver
from CSP import CSPSolver

# Load Sudoku grids from file
def load_grids(filename):
    grids = []
    with open(filename) as f:
        lines = f.readlines()
    
    current_grid = []
    for line in lines:
        line = line.strip()
        if line.startswith("Grid"):  # Start of a new grid
            if current_grid:
                grids.append(current_grid)
                current_grid = []
        else:
            current_grid.append([int(num) for num in line])
    
    if current_grid:
        grids.append(current_grid)  # Add the last grid
    
    return grids

# Load test cases
test_grids = load_grids("p096_sudoku.txt")

# Store statistics
bt_times = []
csp_times = []

# Run Backtracking solver on all test cases
for values in test_grids:
    grid = SudokuGrid([num for row in values for num in row])
    solver = BacktrackingSolver(grid)
    
    start_time = time.time()
    solver.solve()
    end_time = time.time()
    
    bt_times.append(end_time - start_time)

# Run CSP solver on all test cases
for values in test_grids:
    grid = SudokuGrid([num for row in values for num in row])
    solver = CSPSolver(grid)
    
    start_time = time.time()
    solver.solve()
    end_time = time.time()
    
    csp_times.append(end_time - start_time)

# Compute statistics
def print_statistics(name, times):
    print(f"{name} Statistics:")
    print(f"  Total time: {sum(times):.6f} seconds")
    print(f"  Average time: {sum(times) / len(times):.6f} seconds")
    print(f"  Min time: {min(times):.6f} seconds")
    print(f"  Max time: {max(times):.6f} seconds")
    print("")

print_statistics("Backtracking Solver", bt_times)
print_statistics("CSP Solver", csp_times)
