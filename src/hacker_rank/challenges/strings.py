def swap_case(str):
    swap_char_list = []
    for c in str:
        swap_char = c.isupper() and c.lower() or c.upper()
        swap_char_list.append(swap_char)

    return ''.join(swap_char_list)
