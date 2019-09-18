from src.hacker_rank.challenges.arithmetic_operators import arithmetic_operators


def test_arithmetic_operators(capsys):
    arithmetic_operators(2, 3)

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")
    assert spliced_captured_out[0] == "5"
    assert spliced_captured_out[1] == "-1"
    assert spliced_captured_out[2] == "6"
