from src.hacker_rank.challenges.finding_the_percentage import finding_the_percentage


def test_finding_the_percentage(capsys):
    finding_the_percentage('Krishna')
    captured = capsys.readouterr()
    assert  captured.out == '68.00\n'

    finding_the_percentage('Harsh')
    captured = capsys.readouterr()
    assert captured.out == '26.50\n'
