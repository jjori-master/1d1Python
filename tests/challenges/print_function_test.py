from src.hacker_rank.challenges.print_function import print_function


def test_say_hello(capsys):
    print_function(3)
    captured = capsys.readouterr()
    assert captured.out == "123\n"

    print_function(4)
    captured = capsys.readouterr()
    assert captured.out == "1234\n"

    print_function(5)
    captured = capsys.readouterr()
    assert captured.out == "12345\n"
