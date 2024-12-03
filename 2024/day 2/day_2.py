def read_input(file_name: str = 'sample.txt') -> list[str]:
    with open(f'2024/day 2/{file_name}') as file:
        return file.read().strip().split('\n')

def get_reports(lines: list[str]) -> list[list[int]]:
    return [
        list(map(int, line.split()))
        for line in lines
    ]

def is_report_safe(report: list[int]) -> bool:
    level = report[0]
    increasing = level < report[1]
    for next_level in report[1:]:
        is_diff_save = 1 <= abs(level - next_level) <= 3
        is_increasing = level < next_level and increasing is True
        is_decreasing = level > next_level and increasing is False

        if is_diff_save and (is_increasing or is_decreasing):
            level = next_level
            continue
        return False
    return True

def is_report_gracefully_safe(report: list[int]) -> bool:
    if is_report_safe(report):
        return True

    for i in range(0, len(report)):
        if is_report_safe(report[:i] + report[i + 1:]):
            return True
    return False

def solve_part_1(lines: list[str]) -> int:
    return sum(is_report_safe(report) for report in get_reports(lines))

def solve_part_2(lines: list[str]) -> int:
    return sum(is_report_gracefully_safe(report) for report in get_reports(lines))

sample_file = read_input('sample.txt')
input_file = read_input('input.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(sample_file)}')
print(f'Puzzle result: {solve_part_1(input_file)}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(sample_file)}')
print(f'Puzzle result: {solve_part_2(input_file)}')
