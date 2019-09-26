from src.hacker_rank.challenges.tuples_and_hash import tuples_and_hash


def test_tuples_and_hash():
    h = tuples_and_hash('1 2')
    assert h == 3713081631934410656

    h = tuples_and_hash('1 2 3')
    assert h == 2528502973977326415

    h = tuples_and_hash(
        '387 38 498 988 434 282 467 641 464 682 341 586 222 736 187 415 330 323 109 818 78 469 560 623 748 782 352 398 196 39 603 344 630 841 794 994 648 293 861 800 944 249 921 10 781 437 915 451 782 262')
    assert h == 8113509743655314852
