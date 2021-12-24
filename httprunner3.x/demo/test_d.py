import pytest


class TestDemo(object):

    @pytest.mark.parametrize("test_input,expected",
                             [("3+5", 8),
                              ("2+4", 6),
                              ("6 * 9", 54),

                             ])
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected

