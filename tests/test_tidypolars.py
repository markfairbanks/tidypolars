import tidypolars as tp
from tidypolars import col
import polars as pl

def _repeat(x, times):
    if not isinstance(x, list):
        x = [x]
    return x * times

def test_arrange1():
    """Can arrange ascending"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.arrange('y')
    expected = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3]})
    assert actual.frame_equal(expected), "arrange ascending failed"

def test_arrange2():
    """Can arrange descending"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.arrange('x', 'y', desc = [True, False])
    expected = tp.Tibble({'x': ['b', 'a', 'a'], 'y': [3, 1, 2]})
    assert actual.frame_equal(expected), "arrange descending failed"

def test_bind_cols():
    """Can bind_cols"""
    df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3]})
    df2 = tp.Tibble({'z': [4, 4, 4]})
    actual = df1.bind_cols(df2)
    expected = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3], 'z':[4, 4, 4]})
    assert actual.frame_equal(expected), "bind cols failed"

def test_bind_rows():
    """Can bind rows"""
    df1 = tp.Tibble({'x': ['a', 'a'], 'y': [2, 1]})
    df2 = tp.Tibble({'x': ['b'], 'y': [3]})
    actual = df1.bind_rows(df2)
    expected = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    assert actual.frame_equal(expected), "bind rows failed"

def test_distinct_empty():
    """Can distinct columns"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': ['a', 'a', 'b']})
    actual = df.distinct()
    expected = tp.Tibble({'x': ['a', 'b'], 'y': ['a', 'b']})
    assert actual.frame_equal(expected), "empty distinct failed"

def test_distinct_select():
    """Can distinct columns"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.distinct('x')
    expected = tp.Tibble({'x': ['a', 'b']})
    assert actual.frame_equal(expected), "distinct with select failed"

def test_filter():
    """Can filter multiple conditions"""
    df = tp.Tibble({'x': range(10), 'y': range(10)})
    actual = df.filter(col('x') <= 3, col('y') < 2)
    expected = tp.Tibble({'x': range(2), 'y': range(2)})
    assert actual.frame_equal(expected), "filter failed"

def test_mutate():
    """Can edit existing columns and can add columns"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    actual = df.mutate(double_x = col('x') * 2,
                       y = col('y') + 10)
    expected = tp.Tibble(
        {'x': _repeat(1, 3),
         'y': _repeat(12, 3),
          'double_x': _repeat(2, 3)}
    )
    assert actual.frame_equal(expected), "mutate failed"

def test_mutate_across():
    """Can mutate multiple columns simultaneously"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    actual = df.mutate(col(['x', 'y']) * 2,
                       x_plus_y = col('x') + col('y'))
    expected = tp.Tibble(
        {'x': _repeat(2, 3),
         'y': _repeat(4, 3),
         'x_plus_y': _repeat(3, 3)}
    )
    assert actual.frame_equal(expected), "mutate across failed"

def test_pull():
    """Can use pull"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    actual = df.pull('x')
    expected = df.get_column('x')
    assert actual == expected, "pull failed"

def test_relocate():
    """Can relocate columns"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.relocate('y', 'z', before = 'x')
    expected = df.select('y', 'z', 'x')
    assert actual.frame_equal(expected), "relocate failed"

def test_rename():
    """Can rename"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.rename({'x': 'new_x'})
    expected = tp.Tibble({'new_x': range(3), 'y': range(3), 'z': range(3)})
    assert actual.frame_equal(expected), "rename failed"

def test_select():
    """Can select columns"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.select('x', 'z')
    expected = df[['x', 'z']]
    assert actual.frame_equal(expected), "select failed"

def test_slice():
    """Can slice"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice(0, 2)
    expected = tp.Tibble({'x': [0, 2], 'y': ['a', 'b']})
    assert actual.frame_equal(expected), "slice failed"

def test_slice_head():
    """Can slice_head"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice_head(2)
    expected = tp.Tibble({'x': [0, 1], 'y': ['a', 'a']})
    assert actual.frame_equal(expected), "slice_head failed"

def test_slice_tail():
    """Can slice_tail by group"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice_tail(2)
    expected = tp.Tibble({'x': [1, 2], 'y': ['a', 'b']})
    assert actual.frame_equal(expected), "slice_tail failed"

def test_summarize():
    """Can use summarize"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.summarize(avg_x = col('x').mean())
    expected = tp.Tibble({'avg_x': [1]})
    assert actual.frame_equal(expected), "ungrouped summarize failed"

def test_summarize_across():
    """Can use summarize_across"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.summarize(col(['x', 'y']).max().prefix('max_'),
                          avg_x = col('x').mean())
    expected = tp.Tibble({'max_x': [2], 'max_y': [2], 'avg_x': [1]})
    assert actual.frame_equal(expected), "ungrouped summarize across failed"

def test_to_polars():
    """Can convert to a polars DataFrame"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    assert isinstance(df.to_polars(), pl.DataFrame), "to_polars failed"
