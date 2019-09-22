from src.hacker_rank.challenges.strings_split_and_join import strings_split_and_join


def test_strings_split_and_join(capsys):
    strings_split_and_join("hello my name is jjori")
    captured = capsys.readouterr()
    assert captured.out == "hello-my-name-is-jjori\n"
