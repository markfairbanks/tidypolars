import tidypolars as tp
from tidypolars import col

def test_group_filter():
    """Can filter by group"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = (
        df.filter(col('x') <= col('x').mean(),
                  by = 'y')
        .arrange('y')
    )
    expected = tp.Tibble({'x': [0, 2], 'y': ['a', 'b']})
    assert actual.equals(expected), "group filter failed"

def test_group_mutate():
    """Can mutate by group"""
    df = tp.Tibble({'x': range(2), 'y': ['a', 'b']})
    actual = (
        df.mutate(avg_x = col('x').mean(),
                  by = 'y')
        .arrange('y')
    )
    expected = tp.Tibble({'x': [0, 1], 'y': ['a', 'b'], 'avg_x': [0, 1]})
    assert actual.equals(expected), "group mutate failed"

def test_group_slice():
    """Can slice by group"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice(0, by = 'y').arrange('y')
    expected = tp.Tibble({'x': [0, 2], 'y': ['a', 'b']})
    assert actual.equals(expected), "group slice failed"

def test_group_slice_head():
    """Can slice_head by group"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice_head(1, by = 'y').arrange('y')
    expected = tp.Tibble({'x': [0, 2], 'y': ['a', 'b']})
    assert actual.equals(expected), "group slice_head failed"

def test_group_slice_tail():
    """Can slice_tail by group"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice_tail(1, by = 'y').arrange('y')
    expected = tp.Tibble({'x': [1, 2], 'y': ['a', 'b']})
    assert actual.equals(expected), "group slice_tail failed"

def test_group_summarize():
    """Can summarize by group"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.summarize(avg_x = col('x').mean(), by = col('y')).arrange('y')
    expected = tp.Tibble({'y': ['a', 'b'], 'avg_x': [0.5, 2]})
    assert actual.equals(expected), "group summarize failed"

def test_group_summarize_across():
    """Can summarize across by group"""
    df = tp.Tibble({'x': range(3), 'y': range(3, 6), 'z': ['a', 'a', 'b']})
    actual = (
        df
        .summarize(col(['x', 'y']).max().prefix('max_'),
                   avg_x = col('x').mean(),
                   by = [col('z')])
        .arrange('z')
    )
    expected = tp.Tibble({'z': ['a', 'b'],
                          'max_x': [1, 2],
                          'max_y': [4, 5],
                          'avg_x': [0.5, 2]})
    assert actual.equals(expected), "group summarize across failed"