def parse(input_data):
    with open(input_data) as f:
        return [line.strip().split(',') for line in f.readlines()]


def part1():
    lines = parse('input.txt')
    return len([True for line in lines if subset(*get_ranges(line))])


def part2():
    lines = parse('input.txt')
    return len([True for line in lines if not_disjoint(*get_ranges(line))])


def get_ranges(line):
    start_one, end_one = line[0].split('-')
    start_two, end_two = line[1].split('-')
    return range(int(start_one), int(end_one) + 1), range(int(start_two), int(end_two) + 1)


def subset(range_one, range_two):
    range_one, range_two = set(range_one), set(range_two)
    return range_one.issubset(range_two) or range_two.issubset(range_one)


def not_disjoint(range_one, range_two):
    range_one, range_two = set(range_one), set(range_two)
    return not range_one.isdisjoint(range_two) or not range_two.isdisjoint(range_one)
