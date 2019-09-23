from src.hacker_rank.challenges.mutations import mutations


def test_mutations(capsys):
    mutations('abracadabra', 5, 'k')
    captured = capsys.readouterr()
    assert captured.out == 'abrackdabra\n'

    mutations('jjorimister', 6, 'a')
    captured = capsys.readouterr()
    assert captured.out == 'jjorimaster\n'
