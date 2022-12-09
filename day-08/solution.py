from helpers import iterate, parse


ROWS = parse('input.txt')

def part1(): 
    num_edge_trees = (len(ROWS[0]) * 2) + (len(ROWS) * 2) - 4
    return iterate(ROWS) + num_edge_trees


def part2():
    return iterate(ROWS, for_scene=True)
