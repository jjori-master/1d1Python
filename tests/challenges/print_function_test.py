from src.hacker_rank.challenges.print_function import print_function


def test_say_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"