import operator


class MonkeyBiz:
    def __init__(self):
        self.monkey_num = ''
        self.worry_levels = []
        self.operation = ''
        self._div_by = None
        self.true_monkey = ''
        self.false_monkey = '' 
        self.total_inspected = 0    


def calc_monkey_business(num_inspected):
    largest_two = sorted(num_inspected, reverse=True)[:2]
    return largest_two[0] * largest_two[1]


def parse_op(op_str):
    to_do = op_str[op_str.index('=') + 2:]
    if '*' in to_do:
        if to_do[to_do.index('*') + 2:].strip() == 'old': return operator.__mul__, 'same'
        n = int(to_do[to_do.index('*') + 1:].lstrip())
        return operator.__mul__, n
    elif '+' in to_do:
        if to_do[to_do.index('+') + 2:].strip() == 'old': return operator.__add__, 'same'
        n = int(to_do[to_do.index('+') + 1:].lstrip())
        return operator.__add__, n
