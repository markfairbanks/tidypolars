import tidypolars as tp
from tidypolars import col

def test_case_when():
    """Can use case_when"""
    df = tp.Tibble(x = range(1, 4))
    actual = df.mutate(case_x = tp.case_when(col('x') < 2).then(0)
                                .when(col('x') < 3).then(1)
                                .otherwise(0))
    expected = tp.Tibble(x = range(1, 4), case_x = [0, 1, 0])
    assert actual.frame_equal(expected), "case_when failed"

def test_if_else():
    """Can use if_else"""
    df = tp.Tibble(x = range(1, 4))
    actual = df.mutate(case_x = tp.if_else(col('x') < 2, 1, 0))
    expected = tp.Tibble(x = range(1, 4), case_x = [1, 0, 0])
    assert actual.frame_equal(expected), "case_when failed"