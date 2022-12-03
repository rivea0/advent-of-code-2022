RULES = {
    'scores': {'A': 1, 'B': 2, 'C': 3},
    'winning_score': 6,
    'draw_score': 3,
    'shape_to_beat': {'A': 'B', 'B': 'C', 'C': 'A'}
}


def parse(input_data):
    with open(input_data) as f:
        return f.readlines()
    

def part1():
    lines = parse('input.txt')
    # Shapes corresponding to rock (A), paper (B), scissors (C)
    corresponds = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    total_score = 0
    for line in lines:
        their_shape, own_shape = line.split()[0], line.split()[1]
        total_score += RULES['scores'][corresponds[own_shape]]
        if RULES['shape_to_beat'][their_shape] == corresponds[own_shape]:
            total_score += RULES['winning_score']
        elif corresponds[own_shape] == their_shape:
            total_score += RULES['draw_score']

    return total_score


def part2():
    lines = parse('input.txt')
    total_score = 0
    for line in lines:
        their_shape, strategy = line.split()[0], line.split()[1]
        if strategy == 'Z': # To win
            own_shape = RULES['shape_to_beat'][their_shape]
            total_score += RULES['winning_score'] + RULES['scores'][own_shape]
        elif strategy == 'Y': # To draw
            own_shape = their_shape
            total_score += RULES['draw_score'] + RULES['scores'][own_shape] 
        elif strategy == 'X': # To lose
            # Reverse the RULES[shape_to_beat] to find the shape to lose
            own_shape = [key for key in RULES['shape_to_beat'] if their_shape == RULES['shape_to_beat'][key]][0]
            total_score += RULES['scores'][own_shape]

    return total_score
