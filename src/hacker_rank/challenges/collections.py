from collections import Counter


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
