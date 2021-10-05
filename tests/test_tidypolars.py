import tidypolars as tp
from tidypolars import col
import polars as pl

def test_arrange1():
    """Can arrange ascending"""
    df = tp.tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.arrange('y')
    expected = tp.tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3]})
    assert actual.frame_equal(expected), "arrange ascending failed"

def test_arrange2():
    """Can arrange descending"""
    df = tp.tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.arrange('x', 'y', desc = [True, False])
    expected = tp.tibble({'x': ['b', 'a', 'a'], 'y': [3, 1, 2]})
    assert actual.frame_equal(expected), "arrange descending failed"

def test_bind_cols():
    """Can bind_cols"""
    df1 = tp.tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3]})
    df2 = tp.tibble({'z': [4, 4, 4]})
    actual = df1.bind_cols(df2)
    expected = tp.tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3], 'z':[4, 4, 4]})
    assert actual.frame_equal(expected), "bind cols failed"

def test_bind_rows():
    """Can bind rows"""
    df1 = tp.tibble({'x': ['a', 'a'], 'y': [2, 1]})
    df2 = tp.tibble({'x': ['b'], 'y': [3]})
    actual = df1.bind_rows(df2)
    expected = tp.tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    assert actual.frame_equal(expected), "bind rows failed"

def test_distinct():
    """Can bind rows"""
    df = tp.tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.distinct('x')
    expected = tp.tibble({'x': ['a', 'b']})
    assert actual.frame_equal(expected), "distinct failed"

def test_filter():
    """Can filter multiple conditions"""
    df = tp.tibble({'x': range(10), 'y': range(10)})
    actual = df.filter(col('x') <= 3, col('y') < 2)
    expected = tp.tibble({'x': range(2), 'y': range(2)})
    assert actual.frame_equal(expected), "filter failed"

def test_group_by1():
    """Can create grouped_tibble"""
    df = tp.tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    out = df.group_by('y')
    assert isinstance(out, tp.grouped_tibble), "group_by failed"

def test_mutate():
    """Can edit existing columns and can add columns"""
    df = tp.tibble({'x': pl.repeat(1, 3), 'y': pl.repeat(2, 3)})
    actual = df.mutate(double_x = col('x') * 2,
                       y = col('y') + 10)
    expected = tp.tibble(
        {'x': pl.repeat(1, 3),
         'y': pl.repeat(12, 3),
          'double_x': pl.repeat(2, 3)}
    )
    assert actual.frame_equal(expected), "mutate failed"

def test_mutate_across():
    """Can mutate multiple columns simultaneously"""
    df = tp.tibble({'x': pl.repeat(1, 3), 'y': pl.repeat(2, 3)})
    actual = df.mutate(col(['x', 'y']) * 2,
                       x_plus_y = col('x') + col('y'))
    expected = tp.tibble(
        {'x': pl.repeat(2, 3),
         'y': pl.repeat(4, 3),
         'x_plus_y': pl.repeat(3, 3)}
    )
    assert actual.frame_equal(expected), "mutate across failed"

def test_mutate_across():
    """Can use pull"""
    df = tp.tibble({'x': pl.repeat(1, 3), 'y': pl.repeat(2, 3)})
    actual = df.pull('x')
    expected = df.get_column('x')
    assert actual == expected, "pull failed"

def test_relocate():
    """Can relocate columns"""
    df = tp.tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.relocate('y', 'z', before = 'x')
    expected = df.select('y', 'z', 'x')
    assert actual.frame_equal(expected), "relocate failed"

def test_select():
    """Can select columns"""
    df = tp.tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.select('x', 'z')
    expected = df[['x', 'z']]
    assert actual.frame_equal(expected), "select failed"

def test_summarize():
    """Can use summarize"""
    df = tp.tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.summarize(avg_x = col('x').mean())
    expected = tp.tibble({'avg_x': [1]})
    assert actual.frame_equal(expected), "ungrouped summarize failed"

def test_summarize_across():
    """Can use summarize_across"""
    df = tp.tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.summarize(col(['x', 'y']).max().prefix('max_'),
                          avg_x = col('x').mean())
    expected = tp.tibble({'max_x': [2], 'max_y': [2], 'avg_x': [1]})
    assert actual.frame_equal(expected), "ungrouped summarize across failed"
