class SudokuGrid():

    def __init__(self, values=None):
        self.cells = [[0 for _ in range(9)] for _ in range(9)]
        if values is not None:
            self.load_values(values)

    def load_values(self, values):
        if len(values) != 81:
            raise ValueError("List must have exactly 81 elements")
        self.cells = [values[i * 9:(i + 1) * 9] for i in range(9)]

    def print_grid(self, mode="space"):
        if mode not in ["mult", "space", "zero"]:
            raise ValueError("Mode must be 'mult', 'space', or 'zero'")
        modes = {
            "mult": '*',
            "space": " ",
            "zero": 0
        }
        for i, row in enumerate(self.cells):
            if i % 3 == 0 and i != 0:
                print("-" * 23)  
            line = ""
            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    line += " | " 
                line += f"{cell if cell != 0 else modes[mode]} "
            print(line)


    def get_row(self, n):
        if n < 0 or n > 8:
            raise ValueError('Row/Col index must be between 0 and 8')

        return self.cells[n]

    def get_column(self, n):
        if n < 0 or n > 8:
            raise ValueError('Row/Col index must be between 0 and 8')

        return [row[n] for row in self.cells]

    def get_blocks(self):
        answer = []
        for r in range(3):
            for c in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(self.cells[3*r + i][3*c + j])
                answer.append(block)
        return answer
    

    def get_block(self, i, j):
        if i < 0 or i > 8 or j < 0 or j > 8:
            raise ValueError('Row/Col index must be between 0 and 8')

        start_x = i - i % 3
        start_y = j - j % 3
        return [self.cells[start_x + i][start_y + j] for i in range(3) for j in range(3)]
