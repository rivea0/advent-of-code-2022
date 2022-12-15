from itertools import zip_longest
from json import loads


def parse(input_data):
    with open(input_data) as f:        
        all_packets = [loads(line) for line in list(f) if line != '\n']
        return all_packets


def check(left, right):
    for lv, rv in zip_longest(left, right, fillvalue='-'):
        if lv == '-': return True
        if rv == '-': return False
        if type(lv) == int and type(rv) == int:
            if lv != rv:
                return lv < rv
        else:
            left_val = lv if type(lv) == list else [lv]
            right_val = rv if type(rv) == list else [rv]
            result = check(left_val, right_val)
            if result != None: return result


def part1():
    packets = parse('input.txt')
    i = 0
    ordered = []
    packet_num = 1

    for _ in range(len(packets) // 2):
        left, right = packets[i:i + 2][0], packets[i:i + 2][1]
        packet_nums = (packet_num, packet_num + 1)
        if check(left, right): 
            ordered.append(packet_nums[0])
        packet_num += 1
        i += 2

    return sum(ordered)


def part2():
    packets = parse('input.txt')
    # Count all packets that come before [[2]], add 1 for [[2]]'s index
    first_i = sum([1 for packet in packets if check(packet, [[2]])]) + 1
    # Count all packets that come before [[6]],
    # add 2 to include the index of [[2]] as well as [[6]]'s
    second_i = sum([1 for packet in packets if check(packet, [[6]])]) + 2

    return first_i * second_i
