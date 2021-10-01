import tidyframe as tf
from tidyframe import col
import numpy as np

def test_arrange1():
    """Can arrange ascending"""
    df = tf.tidyframe({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.arrange('y')
    expected = tf.tidyframe({'x': ['a', 'a', 'b'], 'y': [1, 2, 3]})
    assert actual.frame_equal(expected), "arrange ascending failed"

def test_arrange2():
    """Can arrange descending"""
    df = tf.tidyframe({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.arrange('x', 'y', desc = [True, False])
    expected = tf.tidyframe({'x': ['b', 'a', 'a'], 'y': [3, 1, 2]})
    assert actual.frame_equal(expected), "arrange descending failed"

def test_filter():
    """Can filter multiple conditions"""
    df = tf.tidyframe({'x': range(10), 'y': range(10)})
    actual = df.filter(col('x') <= 3, col('y') < 2)
    expected = tf.tidyframe({'x': range(2), 'y': range(2)})
    assert actual.frame_equal(expected), "filter failed"

def test_mutate():
    """Can edit existing columns and can add columns"""
    df = tf.tidyframe({'x': np.repeat(1, 3), 'y': np.repeat(2, 3)})
    actual = df.mutate(double_x = col('x') * 2,
                       y = col('y') + 10)
    expected = tf.tidyframe(
        {'x': np.repeat(1, 3),
         'y': np.repeat(12, 3),
          'double_x': np.repeat(2, 3)}
    )
    assert actual.frame_equal(expected), "mutate failed"

def test_relocate():
    """Can relocate columns"""
    df = tf.tidyframe({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.relocate('y', 'z', before = 'x')
    expected = df.select('y', 'z', 'x')
    assert actual.frame_equal(expected), "relocate failed"

def test_select():
    """Can select columns"""
    df = tf.tidyframe({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.select('x', 'z')
    expected = df[['x', 'z']]
    assert actual.frame_equal(expected), "select failed"
