from src.hacker_rank.challenges.loops import loops


def test_loops(capsys):
    N = 5
    loops(N)

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")[:N]

    assert len(spliced_captured_out) == 5

    assert spliced_captured_out[0] == '0'

    assert spliced_captured_out[1] == '1'

    assert spliced_captured_out[2] == '4'

    assert spliced_captured_out[3] == '9'

    assert spliced_captured_out[4] == '16'

