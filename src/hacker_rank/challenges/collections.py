from collections import (Counter, deque)


def shoes_shop(number_of_shoes, customer_needs):
    counter_shoes = Counter(number_of_shoes)
    total_price = 0

    for need in customer_needs:
        need_size = int(need.split(' ')[0])
        need_price = int(need.split(' ')[1])

        shoes_count = counter_shoes[need_size]

        if shoes_count == 0:
            continue

        counter_shoes[need_size] = counter_shoes[need_size] - 1

        total_price += need_price

    return total_price


def calc_deque(operations):
    d = deque()

    for op_group in operations:
        op = op_group.split(' ')[0]
        n = int(op_group.split(' ')[1])

        if op == 'append':
            d.append(n)
            continue

        if op == 'appendleft':
            d.appendleft(n)
            continue

        if op == 'clear':
            d.clear()
            continue

        if op == 'extend':
            d.extend(n)
            continue

        if op == 'extendleft':
            d.extendleft(n)
            continue

        if op == 'pop':
            d.pop()
            continue

        if op == 'popleft':
            d.popleft()
            continue

        if op == 'reverse':
            d.reverse()
            continue

    return d
