def parse(input_data):
    with open(input_data) as f:
        _id = 0
        loads = {_id: 0}
        for line in f.readlines():
            if line == '\n':
                _id += 1
            if line.strip('\n').isdigit():
                loads[_id] = loads.get(_id, 0) + int(line)
    return loads 


def part1():
    loads = parse('input.txt')
    return max(loads.values())


def part2():
    loads = parse('input.txt')
    return sum(sorted(loads.values(), reverse=True)[:3])
