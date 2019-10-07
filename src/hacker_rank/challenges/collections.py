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


# noinspection PyCallingNonCallable
def deque_operator(commands):
    d = deque()

    for command in commands:
        splited_command = command.split(' ')
        c = splited_command[0]

        method_to_call = getattr(d, c)

        if len(splited_command) > 1:
            n = int(splited_command[1])
            method_to_call(n)
            continue

        method_to_call()

    return d
