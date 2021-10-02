import tidypolars as tp
from tidypolars import col
import numpy as np

def test_group_filter():
    """Can filter by group"""
    df = (
        tp.tidyframe({'x': range(3), 'y': ['a', 'a', 'b']})
        .group_by('y')
    )
    actual = df.filter(col('x') <= col('x').mean()).arrange('y')
    expected = tp.tidyframe({'x': [0, 2], 'y': ['a', 'b']})
    assert actual.frame_equal(expected), "group filter failed"

def test_group_mutate():
    """Can mutate by group"""
    df = (
        tp.tidyframe({'x': range(2), 'y': ['a', 'b']})
        .group_by('y')
    )
    actual = df.mutate(avg_x = col('x').mean()).arrange('y')
    expected = tp.tidyframe({'x': [0, 1], 'y': ['a', 'b'], 'avg_x': [0, 1]})
    assert actual.frame_equal(expected), "group mutate failed"

def test_group_summarize():
    """Can summarize by group"""
    df = tp.tidyframe({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.group_by('y').summarize(avg_x = col('x').mean()).arrange('y')
    expected = tp.tidyframe({'y': ['a', 'b'], 'avg_x': [0.5, 2]})
    assert actual.frame_equal(expected), "group summarize failed"

def test_group_summarize_across():
    """Can summarize across by group"""
    df = tp.tidyframe({'x': range(3), 'y': range(3, 6), 'z': ['a', 'a', 'b']})
    actual = (
        df.group_by('z')
        .summarize(col(['x', 'y']).max().prefix('max_'),
                   avg_x = col('x').mean())
        .arrange('z')
    )
    expected = tp.tidyframe({'z': ['a', 'b'],
                             'max_x': [1, 2],
                             'max_y': [4, 5],
                             'avg_x': [0.5, 2]})
    assert actual.frame_equal(expected), "group summarize across failed"