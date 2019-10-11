def lists(list, command):
    splited_command = command.split(' ')
    c = splited_command[0]

    if c == 'print':
        print(list)
        return

    method_to_call = getattr(list, c)

    if len(splited_command) > 2:
        position = int(splited_command[1])
        value = int(splited_command[2])

        method_to_call(position, value)
        return

    if len(splited_command) > 1:
        value = int(splited_command[1])

        method_to_call(value)
        return

    method_to_call()