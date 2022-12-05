def get_instructions(lines):
    for row in lines:
        instructions = row.split()
        number_of_crates_to_move = int(instructions[1])
        from_ = int(instructions[3])
        to = int(instructions[5])
        yield number_of_crates_to_move, from_, to


def remove_items_from_deque(items, d):
    # Remove multiple items from a deque
    for i in items:
        if i in d:
            d.remove(i)
