import math
import sys

from src.hacker_rank.challenges.division import division


def test_division(capsys):
    division(4, 3)

    captured = capsys.readouterr()
    spliced_captured_out = captured.out.split("\n")
    assert spliced_captured_out[0] == "1"

    assert spliced_captured_out[1] == "1.3333333333333333"
