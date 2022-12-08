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


def is_visible(above_trees, right_trees, below_trees, left_trees, tree):
    return not [above_tree for above_tree in above_trees if int(above_tree) >= int(tree)] or \
            not [right_tree for right_tree in right_trees if int(right_tree) >= int(tree)] or \
            not [below_tree for below_tree in below_trees if int(below_tree) >= int(tree)] or \
            not [left_tree for left_tree in left_trees if int(left_tree) >= int(tree)] 


def count_trees_to_see(tree, trees, count):
    for t in trees:
        if int(t) >= int(tree):
            count += 1
            break 
        count += 1
    return count


def measure_viewing_distance(above, right, below, left, tree):
    above_count = below_count = left_count = right_count = 0

    above_count = count_trees_to_see(tree, above[::-1], 0)
    right_count = count_trees_to_see(tree, right, 0)
    below_count = count_trees_to_see(tree, below, 0)
    left_count = count_trees_to_see(tree, left[::-1], 0)

    return above_count * right_count * below_count * left_count


def iterate(rows, for_visibility=False, for_scene=False):
    num_visible_trees = 0
    max_scenic_score = 0

    for row_i, row in enumerate(rows):
        for i, tree in enumerate(row):
            if (is_edge(i, row, rows)):
                continue

            above, right, below, left = find_trees_around(i, row, row_i, rows)

            if is_visible(left, right, above, below, tree):
                num_visible_trees += 1

            score =  measure_viewing_distance(above, right, below, left, tree)
            if score > max_scenic_score:
                max_scenic_score = score

    return num_visible_trees if for_visibility else max_scenic_score
