from src.basic.type_and_operator.calculate import *


class TestCalculate:

    def test_int_to_int_sum(self):
        assert (int_to_int_sum(1, 2)) == 3
        assert (int_to_int_sum(4, 5)) == 9
