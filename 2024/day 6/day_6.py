from pathlib import Path
from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int
    y: int

    def __add__(self, second: 'Coordinate') -> 'Coordinate':
        return Coordinate(self.x + second.x, self.y + second.y)

TDirection = Coordinate

class Guard:
    position: Coordinate
    direction: Coordinate
    path: dict[Coordinate, set[TDirection]]

    def __init__(self, start_position: Coordinate, start_direction: Coordinate):
        self.position = start_position
        self.direction = start_direction
        self.path = dict()

    @property
    def next_position(self) -> Coordinate:
        return self.position + self.direction

    def move(self) -> 'Guard':
        self.path.setdefault(self.position, set()).add(self.direction)
        self.position += self.direction
        return self

    def turn_right(self) -> 'Guard':
        self.path.setdefault(self.position, set()).add(self.direction)
        self.direction = Coordinate(-self.direction.y, self.direction.x)
        return self

    def is_on_map(self, lab_map: list[list]) -> bool:
        map_height, map_width = len(lab_map), len(lab_map[0])
        return 0 <= self.position.x < map_width and 0 <= self.position.y < map_height

    def is_in_loop(self) -> bool:
        return self.direction in self.path.get(self.position, set())

def read_input(file_name: str = 'sample.txt') -> list[list[str]]:
    problem_dir = Path(__file__).parent
    with open(problem_dir / file_name) as file:
        content = file.read().strip().split('\n')
        return [list(row) for row in content]

def get_obstructions_and_guard(lab_map: list[list[str]]) -> tuple[set[Coordinate], Guard]:
    obstructions = set()
    guard = None
    for y, row in enumerate(lab_map):
        for x, cell in enumerate(row):
            if cell == '#':
                obstructions.add(Coordinate(x, y))
            elif cell == '^':
                guard = Guard(Coordinate(x, y), Coordinate(0, -1))
    assert guard is not None
    return obstructions, guard

def simulate(lab_map: list[list[str]], guard: Guard, obstructions: set[Coordinate]) -> Guard:
    while guard.is_on_map(lab_map) and not guard.is_in_loop():
        if guard.next_position in obstructions:
            guard.turn_right()
        else:
            guard.move()
    return guard

def solve_part_1(lab_map: list[list[str]], obstractions: set[Coordinate], guard: Guard) -> int:
    guard = simulate(lab_map, guard, obstractions)
    return len(guard.path)

def solve_part_2(lab_map: list[list[str]], obstractions: set[Coordinate], guard: Guard) -> int:
    start_position = guard.position
    guard = simulate(lab_map, guard, obstractions)
    num_of_loops = 0
    all_possible_obstructions = set(position+direction for position in guard.path for direction in guard.path[position])
    for obstraction in all_possible_obstructions:
        guard_simulation = simulate(lab_map, Guard(start_position, Coordinate(0, -1)), obstractions | {obstraction})
        if guard_simulation.is_in_loop():
            num_of_loops += 1
    return num_of_loops

sample_file = read_input('sample.txt')
input_file = read_input('input.txt')

print('==== Part One ====')
print(f'Sample result: {solve_part_1(sample_file, *get_obstructions_and_guard(sample_file))}')
print(f'Puzzle result: {solve_part_1(input_file, *get_obstructions_and_guard(input_file))}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(sample_file, *get_obstructions_and_guard(sample_file))}')
print(f'Sample result: {solve_part_2(input_file, *get_obstructions_and_guard(input_file))}')
