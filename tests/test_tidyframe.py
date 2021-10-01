import tidyframe as tf
from tidyframe import col

def test_arrange1():
    """Can arrange ascending"""
    df = tf.tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    expected = tf.tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3]})
    actual = df.arrange('y')
    assert actual == expected, "arrange ascending failed"

def test_arrange2():
    """Can arrange descending"""
    df = tf.tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    expected = tf.tibble({'x': ['b', 'a', 'a'], 'y': [3, 1, 2]})
    actual = df.arrange('x', 'y', desc = [False, True])
    assert actual == expected, "arrange ascending failed"
