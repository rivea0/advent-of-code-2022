import re

from math import prod

from helpers import MonkeyBiz, calc_monkey_business, parse_op 


def parse(input_data):
    monkeys = []

    with open(input_data) as f:
        m = MonkeyBiz()
        for line in f.readlines():
            # Add the previous monkey, instantiate new monkey
            if line == '\n':
                monkeys.append(m)
                m = MonkeyBiz()

            monkey_num = re.search('(?<=Monkey )\d', line)
            if monkey_num:
                m.monkey_num = monkey_num.group(0)
            
            worry_levels = re.search('(?<=  Starting items: )[\d]+\s*(?:,\s*(?:\s*[\d])+)*', line)
            if worry_levels:
                m.worry_levels = [n.strip(',') for n in worry_levels.group(0).split()]
                
            operation = re.search('(?<=  Operation: )new = (old|\d{1,2}) (\+|\*) (old|\d{1,2})', line)
            if operation:
                m.operation = parse_op(operation.group(0)) 

            div_by = re.search('(?<=  Test: divisible by )(\d{1,2})', line)
            if div_by: 
                m.div_by = int(div_by.group(0))
            
            true_monkey = re.search('(?<=    If true: throw to monkey )(\d)', line)
            if true_monkey:
                m.true_monkey = true_monkey.group(0)
            
            false_monkey = re.search('(?<=    If false: throw to monkey )(\d)', line)
            if false_monkey:
                m.false_monkey = false_monkey.group(0)
            
        # Add the final monkey
        monkeys.append(m)
        m = MonkeyBiz()

        return monkeys


def do_rounds(calms_down, round_num):
    monkeys = parse('input.txt')
    supermod = prod([_.div_by for _ in monkeys]) # Prevent worry levels from overflow

    for _ in range(round_num):
        for m in monkeys:
            true_m = list(filter(lambda x: x.monkey_num == m.true_monkey, monkeys))[0]
            false_m = list(filter(lambda x: x.monkey_num == m.false_monkey, monkeys))[0]
            for i in m.worry_levels:
                m.total_inspected += 1
                item_level = int(i) 
                op, num = m.operation
                n = item_level if num == 'same' else num 
                if calms_down:
                    op_result = op(int(item_level), n)
                    new_level = op_result // 3
                    if new_level % m.div_by == 0:
                        true_m.worry_levels.append(new_level)
                    else:
                        false_m.worry_levels.append(new_level)
                else:
                    op_result = op((item_level % supermod), (n % supermod))
                    if op_result % m.div_by == 0:
                        true_m.worry_levels.append(op_result)
                    else:
                        false_m.worry_levels.append(op_result)
                m.worry_levels = m.worry_levels[1:]

    return [_.total_inspected for _ in monkeys]


def part1():
    return calc_monkey_business(do_rounds(True, 20))

def part2():
    return calc_monkey_business(do_rounds(False, 10000))
