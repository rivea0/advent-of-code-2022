from string import ascii_letters

PRIORITY_VALUES = {v: i for i, v in enumerate(ascii_letters, start=1)}


def parse(input_data):
    with open(input_data) as f:
        return f.readlines()


def find_common(*args):
    return set.intersection(*args).pop()


def part1():
    sum_priority = 0
    lines = parse('input.txt')
    for line in lines:
        # Get the item that's common in both halves
        common_item =  find_common(set(line[:len(line) // 2]), set(line[len(line) // 2:]))
        sum_priority += PRIORITY_VALUES[common_item]

    return sum_priority


def part2():
    sum_priority = 0
    group = []
    lines = parse('input.txt')
    for i, line in enumerate(lines, start=1):
        group.append(line.strip())
        if i % 3 == 0: # If it's the end of group
            # Get the item that's common among all three elves
            common_item = find_common(set(group[0]), set(group[1]), set(group[2]))
            sum_priority += PRIORITY_VALUES[common_item]
            group = [] # Reset group for the new one
    
    return sum_priority
