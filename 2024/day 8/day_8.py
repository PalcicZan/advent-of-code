from pathlib import Path
from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int
    y: int

    def __add__(self, second: 'Coordinate') -> 'Coordinate':
        return Coordinate(self.x + second.x, self.y + second.y)

    def __sub__(self, second: 'Coordinate') -> 'Coordinate':
        return Coordinate(self.x - second.x, self.y - second.y)

    def __neg__(self) -> 'Coordinate':
        return Coordinate(-self.x, -self.y)

    def is_in_bounds(self, width: int, height: int) -> bool:
        return 0 <= self.x < width and 0 <= self.y < height

def read_input(file_name: str = 'sample.txt') -> list[list[str]]:
    problem_dir = Path(__file__).parent
    with open(problem_dir / file_name) as file:
        content = file.read().strip().split('\n')
        return [list(row) for row in content]

def get_antennas(lines: list[list[str]]) -> dict[str, list[Coordinate]]:
    antennas = dict()
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell != '.':
                antennas.setdefault(cell, []).append(Coordinate(x, y))
    return antennas

def get_antinodes_in_direction(start_antenna: Coordinate, direction: Coordinate, grid: list[list], limit_to_one: bool = True) -> set[Coordinate]:
    antinodes = set()
    height, width = len(grid), len(grid[0])
    while (antinode := start_antenna + direction).is_in_bounds(width, height):
        antinodes.add(antinode)
        if limit_to_one:
            break
        start_antenna = antinode
    return antinodes

def get_antinodes(grid: list[list], antennas: list[Coordinate], limit_to_one: bool = True) -> set[Coordinate]:
    all_pairs = [(antennas[i], antennas[j]) for i in range(len(antennas)) for j in range(i + 1, len(antennas))]
    antinodes = set()
    for (antenna_1, antenna_2) in all_pairs:
        diff = antenna_1 - antenna_2
        if limit_to_one:
            diff = Coordinate(-1, -1)
        antinodes |= get_antinodes_in_direction(antenna_1, -diff, grid, limit_to_one)
        antinodes |= get_antinodes_in_direction(antenna_2, diff, grid, limit_to_one)
    return antinodes

def solve_part_1(grid: list[list], antennas: dict[str, list[Coordinate]]) -> int:
    antinodes = set()
    for frequecy_antennas in antennas.values():
        antinodes |= get_antinodes(grid, frequecy_antennas)
    return len(antinodes)

def solve_part_2(grid: list[list], antennas: dict[str, list[Coordinate]]) -> int:
    antinodes = set()
    for frequecy_antennas in antennas.values():
        antinodes |= get_antinodes(grid, frequecy_antennas, limit_to_one=False)
    return len(antinodes)

sample_file = read_input('sample.txt')
input_file = read_input('input.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(sample_file, get_antennas(sample_file))}')
print(f'Sample result: {solve_part_1(input_file, get_antennas(input_file))}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(sample_file, get_antennas(sample_file))}')
print(f'Sample result: {solve_part_2(input_file, get_antennas(input_file))}')