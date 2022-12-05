from collections import deque
from itertools import islice

from helpers import get_instructions, remove_items_from_deque


def parse(input_data):
    # Indices that letters should be at, if any
    indices = [i for i in range(2, 35, 4)]
    stacks = {i: deque() for i, _ in enumerate(indices, 1)} 
    # Line number that separates the stacks from instructions
    separating_line = 10

    with open(input_data) as f:
        lines = f.readlines()
        # First ten lines are stacks
        for row in lines[:separating_line]: 
            for col_i, char in enumerate(row, start=1):
                if col_i in indices and char.isalpha():
                    stacks[indices.index(col_i) + 1].append(char)
        # Rest of the file is instructions
        instructions = get_instructions(lines[separating_line:])
        
        return stacks, instructions


def part1():
    stacks, instructions = parse('input.txt')
    for num_crates_to_move, from_, to in instructions:
        for _ in range(num_crates_to_move):
            stacks[to].appendleft(stacks[from_].popleft())

    return ''.join([stacks[stack][0] for stack in stacks if stacks[stack]])


def part2():
    stacks, instructions = parse('input.txt')
    for num_crates_to_move, from_, to in instructions:
        crates = deque(islice(stacks[from_], num_crates_to_move))
        stacks[to].extendleft(reversed(crates))
        remove_items_from_deque(crates, stacks[from_])

    return ''.join([stacks[stack][0] for stack in stacks if stacks[stack]])
