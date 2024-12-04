
def read_input(file_name: str = 'sample.txt') -> list[str]:
    with open(f'2024/day 4/{file_name}') as file:
        return file.read().strip().split('\n')

def find_words(matrix: list[list[str]], row: int, column: int, word: str, directions: list[tuple[int, int]]) -> int:
    if matrix[row][column] != word[0]:
        return 0
    count = 0
    for (move_x, move_y) in directions:
        if find_word(matrix, row, column, move_x, move_y, word):
            count += 1
    return count

def find_word(grid: list[list[str]], row: int, column: int, move_x, move_y, word: str) -> bool:
    height, width = len(grid), len(grid[0])
    new_row, new_column = row, column
    i = 0
    while i < len(word):
        if new_row < 0 or new_column < 0 or new_row >= height or new_column >= width:
            return False
        if grid[new_row][new_column] != word[i]:
            return False
        new_row += move_x
        new_column += move_y
        i += 1
    return True

def solve_part_1(lines: list[str]) -> int:
    grid = list(map(list, lines))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    word = 'XMAS'
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            count += find_words(grid, row, column, word, directions)
    return count

def solve_part_2(lines: list[str]) -> int:
    grid = list(map(list, lines))
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            has_xmas = False
            # check for all possible combinations in all directions of the word starting from 'A'
            for word in [('AM', 'AM', 'AS', 'AS'), ('AS', 'AS', 'AM', 'AM'), ('AS', 'AM', 'AS', 'AM'), ('AM', 'AS', 'AM', 'AS')]:
                has_xmas |= find_word(grid, row, column, -1, -1, word[0]) and find_word(grid, row, column, -1, 1,  word[1]) and find_word(grid, row, column, 1, -1, word[2]) and find_word(grid, row, column, 1, 1, word[3])
            count += 1 if has_xmas else 0
    return count

input_file = read_input('input.txt')
sample_file = read_input('sample.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(sample_file)}')
print(f'Puzzle result: {solve_part_1(input_file)}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(sample_file)}')
print(f'Puzzle result: {solve_part_2(input_file)}')