from functools import cmp_to_key

def read_input(file_name: str = 'sample.txt') -> tuple[dict[int, set], list[list[int]]]:
    with open(f'2024/day 5/{file_name}') as file:
        content = file.read().strip().split('\n\n')
        rules_raw, updates_raw = content[0].split('\n'), content[1].split('\n')
        return parse_rules(rules_raw), parse_updates(updates_raw)

def parse_rules(rules_raw: list[str]) -> dict[int, set]:
    rules = {}
    for rule in rules_raw:
        key, value = rule.split('|')
        rules.setdefault(int(key), set()).add(int(value))
    return rules

def parse_updates(updates_raw: list[str]) -> list[list[int]]:
    updates = []
    for update in updates_raw:
        updates.append(list(map(int, update.split(','))))
    return updates

def is_update_valid(update: list[int], rules: dict[int, set]) -> bool:
    before = set()
    for page in update:
        after = rules.get(page, set())
        if after & before:
            return False
        before.add(page)
    return True

def solve_part_1(rules: dict[int, set], updates: list[list[int]]) -> int:
    sum_of_valid = 0
    for update in updates:
        if is_update_valid(update, rules):
            sum_of_valid += update[len(update)//2]
    return sum_of_valid

def solve_part_2(rules: dict[int, set], updates: list[list[int]]) -> int:
    sum_of_invalid = 0
    for update in updates:
        if not is_update_valid(update, rules):
            def compare(x, y):
                return 1 if y in rules.get(x, set()) else -1
            sorted_update = sorted(update, key=cmp_to_key(compare))
            sum_of_invalid += sorted_update[len(sorted_update)//2]
    return sum_of_invalid

print('==== Part One ====')
print(f'Sample result: {solve_part_1(*read_input("sample.txt"))}')
print(f'Puzzle result: {solve_part_1(*read_input("input.txt"))}')

print('==== Part Two ====')
print(f'Sample result: {solve_part_2(*read_input("sample.txt"))}')
print(f'Sample result: {solve_part_2(*read_input("input.txt"))}')