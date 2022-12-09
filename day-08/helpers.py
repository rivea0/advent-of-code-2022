# WARNING: Coding horror ahead.

def parse(input_data):
    with open(input_data) as f:
        return [line.strip('\n') for line in f]


def find_trees_around(index_, row, row_index, rows):
    above_trees = [r[index_] for r in rows[:row_index]]
    right_trees = row[index_ + 1:]
    below_trees = [r[index_] for r in rows[row_index + 1:]]
    left_trees = row[:index_]

    return above_trees, right_trees, below_trees, left_trees


def is_edge(idx, row, rows):
    return ((rows.index(row) == 0 or rows.index(row) == len(rows) - 1)
            or (idx == 0 or idx == len(row) - 1))


def check_tall_trees(trees, tree):
    return [t for t in trees if int(t) >= int(tree)]


def is_visible(above_trees, right_trees, below_trees, left_trees, tree):
    return not check_tall_trees(above_trees, tree) or not check_tall_trees(right_trees, tree) or \
            not check_tall_trees(below_trees, tree) or not check_tall_trees(left_trees, tree)


def count_trees_to_see(trees, tree, count=0):
    for t in trees:
        if int(t) >= int(tree):
            count += 1
            break
        count += 1
    return count


def measure_viewing_distance(above, right, below, left, tree):
    above_count = below_count = left_count = right_count = 0

    above_count = count_trees_to_see(above[::-1], tree)
    right_count = count_trees_to_see(right, tree)
    below_count = count_trees_to_see(below, tree)
    left_count = count_trees_to_see(left[::-1], tree)

    return above_count * right_count * below_count * left_count


def iterate(rows, for_scene=False):
    num_visible_trees = 0
    max_scenic_score = 0

    for row_i, row in enumerate(rows):
        for i, tree in enumerate(row):
            if (is_edge(i, row, rows)):
                continue

            above, right, below, left = find_trees_around(i, row, row_i, rows)

            if is_visible(above, right, below, left, tree):
                num_visible_trees += 1

            score =  measure_viewing_distance(above, right, below, left, tree)
            if score > max_scenic_score:
                max_scenic_score = score

    return max_scenic_score if for_scene else num_visible_trees
