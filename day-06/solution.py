def parse(input_data, marker):
    with open(input_data) as f:
        content = f.read()
        return next(i + marker for i, _ in enumerate(content) if len(set(content[i:i + marker])) == marker)


def part1():
    return parse('input.txt', 4)


def part2():
    return parse('input.txt', 14)    
