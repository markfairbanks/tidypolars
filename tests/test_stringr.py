import tidypolars as tp
from tidypolars import col

def test_paste():
    """Can use paste"""
    df = tp.Tibble(x = ['a', 'b', 'c'])
    actual = df.mutate(x_end = tp.paste(col('x'), 'end', sep = '_'))
    expected = tp.Tibble(x = ['a', 'b', 'c'], x_end = ['a_end', 'b_end', 'c_end'])
    assert actual.frame_equal(expected), "paste failed"

def test_paste0():
    """Can use paste0"""
    df = tp.Tibble(x = ['a', 'b', 'c'])
    actual = df.mutate(x_end = tp.paste0(col('x'), '_end'))
    expected = tp.Tibble(x = ['a', 'b', 'c'], x_end = ['a_end', 'b_end', 'c_end'])
    assert actual.frame_equal(expected), "paste0 failed"

def test_str_detect_single():
    """Can str_detect find a single string"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_detect('name', 'a'),
                       y = tp.str_detect('name', 'a', negate=True))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                         x = [True, True, True, True], 
                         y = [False, False, False, False])
    assert actual.frame_equal(expected), "str_detect single failed"

def test_str_detect_multiple():
    """Can str_detect find multiple strings"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_detect('name', ['a', 'e']), 
                       y = tp.str_detect('name', ['a', 'e'], negate=True))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                         x = [True, False, True, True], 
                         y = [False, True, False, False])
    assert actual.frame_equal(expected), "str_detect multiple failed"

def test_str_extract():
    """Can str_extract extract strings"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_extract('name', 'pp'))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                         x = ['pp', None, None, None])
    assert actual.frame_equal(expected), "str_extract failed"

def test_str_length():
    """Can str_length count strings"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_length('name'))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                        x = [5, 6, 4, 5])
    assert actual.frame_equal(expected), "str_length failed"

def test_str_sub():
    """Can str_sub can extract strings"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_sub('name', 0, 3))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                        x = ['app', 'ban', 'pea', 'gra'])
    assert actual.frame_equal(expected), "str_sub failed"

def test_str_remove_all():
    """Can str_remove_all find all strings and remove"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_remove_all(tp.col('name'), 'a'))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['pple', 'bnn', 'per', 'grpe'])
    assert actual.frame_equal(expected), "str_remove_all failed"

def test_str_remove():
    """Can str_remove finds first instance of string and remove"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_remove(tp.col('name'), 'a'))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['pple', 'bnana', 'per', 'grpe'])
    assert actual.frame_equal(expected), "str_remove failed"

def test_str_replace_all():
    """Can str_replace_all find all strings and replace"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_replace_all(tp.col('name'), 'a', 'A'))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['Apple', 'bAnAnA', 'peAr', 'grApe'])
    assert actual.frame_equal(expected), "str_replace_all failed"

def test_str_replace():
    """Can str_replace finds first instance of string and replace"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_replace(tp.col('name'), 'a', 'A'))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['Apple', 'bAnana', 'peAr', 'grApe'])
    assert actual.frame_equal(expected), "str_replace failed"

def test_str_to_lower():
    """Can str_to_lower lowercase a string"""
    df = tp.Tibble(name = ['APPLE', 'BANANA', 'PEAR', 'GRAPE'])
    actual = df.mutate(name = tp.str_to_lower(tp.col('name')))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    assert actual.frame_equal(expected), "str_to_lower failed"

def test_str_to_upper():
    """Can str_to_upper uppercase a string"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(name = tp.str_to_upper(tp.col('name')))
    expected = tp.Tibble(name = ['APPLE', 'BANANA', 'PEAR', 'GRAPE'])
    assert actual.frame_equal(expected), "str_to_upper failed"

def test_str_trim():
    """Can str_to_upper uppercase a string"""
    df = tp.Tibble(x = [' a ', ' b ', ' c '])
    actual = (
        df.mutate(both = tp.str_trim('x'),
                  left = tp.str_trim('x', "left"),
                  right = tp.str_trim('x', "right"))
        .drop('x')
    )
    expected = tp.Tibble(
        both = ['a', 'b', 'c'],
        left = ['a ', 'b ', 'c '],
        right = [' a', ' b', ' c']
    )
    assert actual.frame_equal(expected), "str_trim failed"