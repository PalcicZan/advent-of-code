from functools import reduce
import re

def read_input(file_name: str = 'sample.txt') -> list[str]:
    with open(f'2024/day 3/{file_name}') as file:
        return file.read().strip().split('\n')

def sum_of_mul(line: str) -> int:
    MUL_REGEX = r'mul\(\d+\,\d+\)'
    NUM_REGEX = r'\d+'
    sum_of_product = 0
    for match in re.findall(MUL_REGEX, line):
        sum_of_product += reduce(lambda x, y: x * y, map(int, re.findall(NUM_REGEX, match)))
    return sum_of_product

def solve_part_1(lines: list[str]) -> int:
    program = ''.join(lines)
    return sum_of_mul(program)

def solve_part_2(lines: list[str]) -> int:
    BAD_PART_REGEX = r'don\'t\(\).*?(do\(\)|$)'
    program = ''.join(lines)
    fixed_program = re.sub(BAD_PART_REGEX, '', program)
    return sum_of_mul(fixed_program)

input_file = read_input('input.txt')
sample_file = read_input('sample.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(sample_file)}')
print(f'Puzzle result: {solve_part_1(input_file)}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(sample_file)}')
print(f'Puzzle result: {solve_part_2(input_file)}')