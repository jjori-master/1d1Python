from src.hacker_rank.challenges.basic_data_types import *


def test_lists(capsys):
    commands = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print',
                'pop', 'reverse', 'print']

    list = []
    for command in commands:
        lists(list, command)

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")[:3]

    assert spliced_captured_out[0] == '[6, 5, 10]'
    assert spliced_captured_out[1] == '[1, 5, 9, 10]'
    assert spliced_captured_out[2] == '[9, 5, 1]'
