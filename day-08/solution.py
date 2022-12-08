from helpers import iterate, parse


ROWS = parse('input.txt')

def part1(): 
    num_edge_trees = (len(ROWS[0]) * 2) + (len(ROWS) * 2) - 4
    # Main concern is visibility
    return iterate(ROWS, for_visibility=True) + num_edge_trees


def part2():
    # Main concern is the scene
    return iterate(ROWS, for_scene=True)
