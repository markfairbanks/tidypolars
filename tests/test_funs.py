import tidypolars as tp
from tidypolars import col
import polars.selectors as cs
import math

def test_abs():
    """Can get absolute value"""
    df = tp.tibble(x = range(-3, 0))
    actual = df.mutate(abs_x = tp.abs('x'), abs_col_x = tp.abs(col('x')))
    expected = tp.tibble(x = range(-3, 0), abs_x = range(3, 0, -1), abs_col_x = range(3, 0, -1))
    assert actual.equals(expected), "abs failed"

def test_agg_stats():
    """Can get aggregation statistics"""
    df = tp.tibble(x = range(3), y = [2, 1, 0])
    actual = (
        df
        .summarize(
            corr = tp.cor('x', 'y'),
            count_x = tp.count('x'), count_col_x = tp.count(col('x')),
            cov = tp.cov('x', 'y'),
            first_x = tp.first('x'), first_col_x = tp.first(col('x')),
            last_x = tp.last('x'), last_col_x = tp.last(col('x')),
            max_x = tp.max('x'), max_col_x = tp.max(col('x')),
            mean_x = tp.mean('x'), mean_col_x = tp.mean(col('x')),
            median_x = tp.median('x'), median_col_x = tp.median(col('x')),
            min_x = tp.min('x'), min_col_x = tp.min(col('x')),
            n = tp.n(),
            n_distinct_x = tp.n_distinct('x'), n_distinct_col_x = tp.n_distinct(col('x')),
            quantile_x = tp.quantile('x', .25),
            sd_x = tp.sd('x'), sd_col_x = tp.sd(col('x')),
            sum_x = tp.sum('x'), sum_col_x = tp.sum(col('x')),
            var_y = tp.var('y')
        )
        .mutate(tp.as_integer(cs.numeric().as_expr()))
    )
    expected = tp.tibble(
        corr = [-1],
        count_x = [3], count_col_x = [3],
        cov = [-1],
        first_x = [0], first_col_x = [0],
        last_x = [2], last_col_x = [2],
        max_x = [2], max_col_x = [2],
        mean_x = [1], mean_col_x = [1],
        median_x = [1], median_col_x = [1],
        min_x = [0], min_col_x = [0],
        n = [3],
        n_distinct_x = [3], n_distinct_col_x = [3],
        quantile_x = [1],
        sd_x = [1], sd_col_x = [1],
        sum_x = [3], sum_col_x = [3],
        var_y = [1]
    )
    assert actual.equals(expected), "aggregation stats failed"

def test_case_when():
    """Can use case_when"""
    df = tp.tibble(x = range(1, 4))
    actual = df.mutate(case_x = tp.case_when(col('x') < 2).then(0)
                                .when(col('x') < 3).then(1)
                                .otherwise(0))
    expected = tp.tibble(x = range(1, 4), case_x = [0, 1, 0])
    assert actual.equals(expected), "case_when failed"

def test_casting():
    """Can do type casting"""
    df = tp.tibble(int_col = [0, 0, 1], float_col = [1.0, 2.0, 3.0], chr_col = ["1", "2", "3"])
    actual = (
        df
        .mutate(float_cast = tp.as_float('int_col'),
                int_cast = tp.as_integer('float_col'),
                string_cast = tp.as_string('int_col'),
                bool_cast = tp.as_boolean('int_col'))
        .select('float_cast', 'int_cast', 'string_cast', 'bool_cast')
    )
    expected = tp.tibble(float_cast = [0.0, 0.0, 1.0],
                         int_cast = [1, 2, 3],
                         string_cast = ["0", "0", "1"],
                         bool_cast = [False, False, True])
    assert actual.equals(expected), "casting failed"

def test_coalesce():
    """Can use coalesce"""
    df = tp.tibble(x = [None, None, 1], y = [2, None, 2], z = [3, 3, 3])
    actual = (
        df
        .mutate(
            coalesce_x = tp.coalesce(col('x'), col('y'), col('z'))
        )
        .select('coalesce_x')
    )
    expected = tp.tibble(coalesce_x = [2, 3, 1])
    assert actual.equals(expected), "coalesce failed"

def test_floor():
    """Can get the floor"""
    df = tp.tibble(x = [1.1, 5.5])
    actual = df.mutate(floor_x = tp.floor('x')).select('floor_x')
    expected = tp.tibble(floor_x = [1.0, 5.0])
    assert actual.equals(expected), "floor failed"

def test_lag():
    """Can get lagging values with function"""
    df = tp.tibble({'x': range(3)})
    actual = df.mutate(lag_null = tp.lag(col('x')),
                       lag_default = tp.lag('x', default = 1))
    expected = tp.tibble({'x': range(3),
                          'lag_null': [None, 0, 1],
                          'lag_default': [1, 0, 1]})
    assert actual.equals(expected, null_equal = True), "lag failed"

def test_lead():
    """Can get leading values with function"""
    df = tp.tibble({'x': range(3)})
    actual = df.mutate(lead_null = tp.lead(col('x')),
                       lead_default = tp.lead('x', default = 1))
    expected = tp.tibble({'x': range(3),
                          'lead_null': [1, 2, None],
                          'lead_default': [1, 2, 1]})
    assert actual.equals(expected, null_equal = True), "lead failed"

def test_logs():
    """Can get leading values with function"""
    df = tp.tibble({'x': range(1, 4)})
    actual = df.mutate(log = tp.log(col('x')).round(2),
                       log10 = tp.log10('x').round(2))
    expected = df.mutate(log = col('x').log().round(2), log10 = col('x').log10().round(2))
    assert actual.equals(expected), "log failed"

def test_if_else():
    """Can use if_else"""
    df = tp.tibble(x = range(1, 4))
    actual = df.mutate(case_x = tp.if_else(col('x') < 2, 1, 0))
    expected = tp.tibble(x = range(1, 4), case_x = [1, 0, 0])
    assert actual.equals(expected), "if_else failed"

def test_is_predicates():
    """Can use is predicates"""
    df = tp.tibble(x = [0.0, 1.0, 2.0],
                   y = [None, math.inf, math.nan])
    actual = (
        df
        .mutate(
            between = tp.between('x', 1, 2),
            is_finite = tp.is_finite('x'),
            is_in = tp.is_in('x', [1.0, 2.0]),
            is_infinite = tp.is_infinite('y'),
            is_not = tp.is_not(tp.is_finite(col('x'))),
            is_not_in = tp.is_not_in('x', [1.0, 2.0]),
            is_not_null = tp.is_not_null('y'),
            is_null = tp.is_null('y')

        )
    ).drop(['x', 'y'])
    expected = tp.tibble(
        between = [False, True, True],
        is_finite = [True, True, True],
        is_in = [False, True, True],
        is_infinite = [None, True, False],
        is_not = [False, False, False],
        is_not_in = [True, False, False],
        is_not_null = [False, True, True],
        is_null = [True, False, False]
    )
    assert actual.equals(expected, null_equal = True), "is_predicates failed"

def test_rep():
    df = tp.tibble(x = [0, 1], y = [0, 1])
    assert tp.rep(df, 2).equals(df.bind_rows(df)), "rep df failed"
    assert tp.rep(1, 2).equals(tp.Series([1, 1])), "rep int failed"
    assert tp.rep("a", 2).equals(tp.Series(["a", "a"])), "rep str failed"
    assert tp.rep(True, 2).equals(tp.Series([True, True])), "rep bool failed"
    assert tp.rep(tp.Series([0, 1]), 2).equals(tp.Series([0, 1, 0, 1])), "rep series failed"

def test_replace_null():
    """Can replace nulls"""
    df = tp.tibble(x = [0, None], y = [None, None])
    actual = df.mutate(x = tp.replace_null(col('x'), 1))
    expected = tp.tibble(x = [0, 1], y = [None, None])
    assert actual.equals(expected), "replace_null function failed"

def test_row_number():
    """Can get row number"""
    df = tp.tibble(x = ['a', 'a', 'b'])
    actual = df.mutate(row_num = tp.row_number())
    expected = tp.tibble(x = ['a', 'a', 'b'], row_num = [1, 2, 3])
    assert actual.equals(expected), "row_number failed"

def test_row_number_group():
    """Can get row number by group"""
    df = tp.tibble(x = ['a', 'a', 'b'])
    actual = (
        df.mutate(group_row_num = tp.row_number(), _by = 'x')
        .arrange('x', 'group_row_num')
    )
    expected = tp.tibble(x = ['a', 'a', 'b'], group_row_num = [1, 2, 1])
    assert actual.equals(expected), "group row_number failed"

def test_round():
    """Can round values"""
    df = tp.tibble(x = [1.11, 2.22, 3.33])
    actual = df.mutate(x = tp.round(col('x'), 1))
    expected = tp.tibble(x = [1.1, 2.2, 3.3])
    assert actual.equals(expected), "round failed"

def test_sqrt():
    """Can get the square root"""
    df = tp.tibble(x = [9, 25, 100])
    actual = df.mutate(x = tp.sqrt('x'))
    expected = tp.tibble(x = [3, 5, 10])
    assert actual.equals(expected), "sqrt failed"