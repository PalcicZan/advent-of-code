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

class Grid:
    def __init__(self, grid: list[list[str]], limit_to_one: bool = True):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.limit_to_one = limit_to_one

    def __contains__(self, coordinate: Coordinate) -> bool:
        return 0 <= coordinate.x < self.width and 0 <= coordinate.y < self.height

    def get_antennas(self) -> dict[str, list[Coordinate]]:
        antennas = dict()
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                if cell != '.':
                    antennas.setdefault(cell, []).append(Coordinate(x, y))
        return antennas

    def get_antinodes(self, antennas: list[Coordinate]) -> set[Coordinate]:
        all_pairs = [(antennas[i], antennas[j]) for i in range(len(antennas)) for j in range(i + 1, len(antennas))]
        antinodes = set()
        for (antenna_1, antenna_2) in all_pairs:
            diff = antenna_1 - antenna_2
            if self.limit_to_one:
                diff = Coordinate(-1, -1)
            antinodes |= self.get_antinodes_in_direction(antenna_1, -diff)
            antinodes |= self.get_antinodes_in_direction(antenna_2, diff)
        return antinodes

    def get_antinodes_in_direction(self, start_antenna: Coordinate, direction: Coordinate) -> set[Coordinate]:
        antinodes = set()
        while (antinode := start_antenna + direction) in self:
            antinodes.add(antinode)
            if self.limit_to_one:
                break
            start_antenna = antinode
        return antinodes

def read_input(file_name: str = 'sample.txt') -> list[list[str]]:
    problem_dir = Path(__file__).parent
    with open(problem_dir / file_name) as file:
        content = file.read().strip().split('\n')
        return [list(row) for row in content]

def solve_part_1(grid_values: list[list[str]]) -> int:
    return count_all_antinodes(Grid(grid_values))

def solve_part_2(grid_values: list[list]) -> int:
    return count_all_antinodes(Grid(grid_values, limit_to_one=False))

def count_all_antinodes(grid: Grid) -> int:
    antinodes = set()
    for frequecy_antennas in grid.get_antennas().values():
        antinodes |= grid.get_antinodes(frequecy_antennas)
    return len(antinodes)

sample_file = read_input('sample.txt')
input_file = read_input('input.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(sample_file)}')
print(f'Sample result: {solve_part_1(input_file)}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(sample_file)}')
print(f'Sample result: {solve_part_2(input_file)}')