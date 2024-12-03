from collections import Counter

def read_input(file_name: str = 'sample.txt') -> list[str]:
    with open(f'2024/{file_name}') as file:
        return file.read().strip().split('\n')

def get_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    left_list, right_list = [], []
    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    return left_list, right_list

def solve_part_1(lines: list[str]) -> int:
    # could use one liner - sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list)))
    left_list, right_list = get_lists(lines)
    sum_of_diff = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        sum_of_diff += abs(left - right)
    return sum_of_diff


def solve_part_2(lines: list[str]) -> int:
    # could use one liner - sum(left * right_list_count[left] for left in left_list)
    left_list, right_list = get_lists(lines)
    right_list_count = Counter(right_list)
    similarity_score = 0
    for left in left_list:
        similarity_score += left * right_list_count[left]
    return similarity_score

input_file = read_input('input.txt')
sample_file = read_input('sample.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(sample_file)}')
print(f'Puzzle result: {solve_part_1(input_file)}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(sample_file)}')
print(f'Puzzle result: {solve_part_2(input_file)}')