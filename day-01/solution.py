def parse(input_data):
    with open(input_data) as f:
        id_ = 0
        loads = {id_: 0}
        for line in f.readlines():
            if line == '\n':
                id_ += 1
            if line.strip('\n').isdigit():
                loads[id_] = loads.get(id_, 0) + int(line)
    return loads 


def part1():
    loads = parse('input.txt')
    return max(loads.values())


def part2():
    loads = parse('input.txt')
    return sum(sorted(loads.values(), reverse=True)[:3])
