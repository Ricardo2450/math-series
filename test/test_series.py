import pytest
from series.series import fibonacci, lucas, sum_series


def test_fibonacci():
    assert fibonacci(9) == 34
    assert fibonacci(13) == 233



def test_lucas():
    assert lucas(3) == 4
    assert lucas(0) == 2
    assert lucas(1) == 1


def test_sum_series():
    assert sum_series(9) == 34
    assert sum_series(3,2,1) == 4
