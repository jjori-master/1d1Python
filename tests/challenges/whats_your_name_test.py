from src.hacker_rank.challenges.whats_your_name import whats_your_name


def test_whats_your_name(capsys):
    whats_your_name('Ross', 'Taylor')
    captured = capsys.readouterr()
    assert captured.out == 'Hello Ross Taylor! You just delved into python.\n'

    whats_your_name('jjori', 'master')
    captured = capsys.readouterr()
    assert captured.out == 'Hello jjori master! You just delved into python.\n'
