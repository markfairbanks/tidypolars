import tidypolars as tp
from tidypolars import col

def test_agg_stats():
    """Can get aggregation statistics"""
    df = tp.Tibble(x = range(3))
    actual = (
        df
        .summarize(
            max_x = tp.max('x'), max_col_x = tp.max(col('x')),
            mean_x = tp.mean('x'), mean_col_x = tp.mean(col('x')),
            median_x = tp.median('x'), median_col_x = tp.median(col('x')),
            min_x = tp.min('x'), min_col_x = tp.min(col('x')),
            n_distinct_x = tp.n_distinct('x'), n_distinct_col_x = tp.n_distinct(col('x')),
            sd_x = tp.sd('x'), sd_col_x = tp.sd(col('x')),
            sum_x = tp.sum('x'), sum_col_x = tp.sum(col('x')),
        )
    )
    expected = tp.Tibble(
        max_x = [2], max_col_x = [2],
        mean_x = [1], mean_col_x = [1],
        median_x = [1], median_col_x = [1],
        min_x = [0], min_col_x = [0],
        n_distinct_x = [3], n_distinct_col_x = [3],
        sd_x = [1], sd_col_x = [1],
        sum_x = [3], sum_col_x = [3],
    )
    assert actual.frame_equal(expected), "aggregation stats failed"

def test_case_when():
    """Can use case_when"""
    df = tp.Tibble(x = range(1, 4))
    actual = df.mutate(case_x = tp.case_when(col('x') < 2).then(0)
                                .when(col('x') < 3).then(1)
                                .otherwise(0))
    expected = tp.Tibble(x = range(1, 4), case_x = [0, 1, 0])
    assert actual.frame_equal(expected), "case_when failed"

def test_lag():
    """Can get lagging values with function"""
    df = tp.Tibble({'x': range(3)})
    actual = df.mutate(lag_null = tp.lag(col('x')),
                       lag_default = tp.lag('x', default = 1))
    expected = tp.Tibble({'x': range(3),
                          'lag_null': [None, 0, 1],
                          'lag_default': [1, 0, 1]})
    assert actual.frame_equal(expected, null_equal = True), "lag failed"

def test_lead():
    """Can get leading values with function"""
    df = tp.Tibble({'x': range(3)})
    actual = df.mutate(lead_null = tp.lead(col('x')),
                       lead_default = tp.lead('x', default = 1))
    expected = tp.Tibble({'x': range(3),
                          'lead_null': [1, 2, None],
                          'lead_default': [1, 2, 1]})
    assert actual.frame_equal(expected, null_equal = True), "lead failed"

def test_if_else():
    """Can use if_else"""
    df = tp.Tibble(x = range(1, 4))
    actual = df.mutate(case_x = tp.if_else(col('x') < 2, 1, 0))
    expected = tp.Tibble(x = range(1, 4), case_x = [1, 0, 0])
    assert actual.frame_equal(expected), "case_when failed"