from pathlib import Path

class EquationSolver:

    def __init__(self, target_value: int, equation: list[int], operations: list[str]):
        self.target_value = target_value
        self.equation = equation
        self.operations = operations

    def is_solvable(self) -> bool:
        first_value = self.equation[0]
        return self.solve_equation(self.equation[1:], first_value)

    def solve_equation(self, left_equation: list[int], computed: int) -> bool:
        if computed == self.target_value and not left_equation:
            return True

        if computed > self.target_value or not left_equation:
            return False

        for operation in self.operations:
            if operation == '+':
                new_value = computed + left_equation[0]
            elif operation == '*':
                new_value = computed * left_equation[0]
            elif operation == '||':
                new_value = int(str(computed) + str(left_equation[0]))

            if self.solve_equation(left_equation[1:], new_value):
                return True
        return False

def read_input(file_name: str = 'sample.txt') -> list[str]:
    problem_dir = Path(__file__).parent
    with open(problem_dir / file_name) as file:
        return file.read().strip().split('\n')

def get_equations(lines: list[str]) -> list[tuple]:
    equations = []
    for line in lines:
        target, equation = line.split(': ')
        equations.append((int(target), list(map(int, equation.split(' ')))))
    return equations

def solve_equations(equations: list[tuple], operations: list[str]) -> int:
    sum_of_valid_equations = 0
    for (target, equation) in equations:
        if EquationSolver(target, equation, operations).is_solvable():
            sum_of_valid_equations += target
    return sum_of_valid_equations

def solve_part_1(equations: list[tuple]) -> int:
    return solve_equations(equations, operations=['*', '+'])

def solve_part_2(equations: list[tuple]) -> int:
    return solve_equations(equations, operations=['*', '+', '||'])

sample_file = read_input('sample.txt')
input_file = read_input('input.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(get_equations(sample_file))}')
print(f'Sample result: {solve_part_1(get_equations(input_file))}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(get_equations(sample_file))}')
print(f'Sample result: {solve_part_2(get_equations(input_file))}')