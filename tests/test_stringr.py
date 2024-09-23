import tidypolars as tp
from tidypolars import col

def test_paste():
    """Can use paste"""
    df = tp.tibble(x = ['a', 'b', 'c'])
    actual = df.mutate(x_end = tp.paste(col('x'), 'end', sep = '_'))
    expected = tp.tibble(x = ['a', 'b', 'c'], x_end = ['a_end', 'b_end', 'c_end'])
    assert actual.equals(expected), "paste failed"

def test_paste0():
    """Can use paste0"""
    df = tp.tibble(x = ['a', 'b', 'c'])
    actual = df.mutate(x_end = tp.paste0(col('x'), '_end'))
    expected = tp.tibble(x = ['a', 'b', 'c'], x_end = ['a_end', 'b_end', 'c_end'])
    assert actual.equals(expected), "paste0 failed"

def test_str_c():
    """Can use str_c"""
    df = tp.tibble(x = ['a', 'b', 'c'])
    actual = df.mutate(x_end = tp.str_c(col('x'), 'end', sep = '_'))
    expected = tp.tibble(x = ['a', 'b', 'c'], x_end = ['a_end', 'b_end', 'c_end'])
    assert actual.equals(expected), "str_c failed"

def test_str_detect_single():
    """Can str_detect find a single string"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_detect('name', 'a'),
                       y = tp.str_detect('name', 'a', negate=True))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                         x = [True, True, True, True], 
                         y = [False, False, False, False])
    assert actual.equals(expected), "str_detect single failed"

def test_str_detect_multiple():
    """Can str_detect find multiple strings"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_detect('name', ['a', 'e']), 
                       y = tp.str_detect('name', ['a', 'e'], negate=True))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                         x = [True, False, True, True], 
                         y = [False, True, False, False])
    assert actual.equals(expected), "str_detect multiple failed"

def test_str_ends():
    """Can use str_end"""
    df = tp.tibble(words = ['apple', 'bear', 'amazing'])
    actual = df.filter(tp.str_ends(col('words'), 'ing'))
    expected = tp.tibble(words = ['amazing'])
    assert actual.equals(expected), "str_ends failed"

def test_str_extract():
    """Can str_extract extract strings"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_extract('name', 'pp'))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                         x = ['pp', None, None, None])
    assert actual.equals(expected), "str_extract failed"

def test_str_length():
    """Can str_length count strings"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_length('name'))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                        x = [5, 6, 4, 5])
    assert actual.equals(expected), "str_length failed"

def test_str_sub():
    """Can str_sub can extract strings"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(x = tp.str_sub('name', 0, 3))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                        x = ['app', 'ban', 'pea', 'gra'])
    assert actual.equals(expected), "str_sub failed"

def test_str_remove_all():
    """Can str_remove_all find all strings and remove"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_remove_all(tp.col('name'), 'a'))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['pple', 'bnn', 'per', 'grpe'])
    assert actual.equals(expected), "str_remove_all failed"

def test_str_remove():
    """Can str_remove finds first instance of string and remove"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_remove(tp.col('name'), 'a'))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['pple', 'bnana', 'per', 'grpe'])
    assert actual.equals(expected), "str_remove failed"

def test_str_replace_all():
    """Can str_replace_all find all strings and replace"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_replace_all(tp.col('name'), 'a', 'A'))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['Apple', 'bAnAnA', 'peAr', 'grApe'])
    assert actual.equals(expected), "str_replace_all failed"

def test_str_replace():
    """Can str_replace finds first instance of string and replace"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(new_name = tp.str_replace(tp.col('name'), 'a', 'A'))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'], new_name = ['Apple', 'bAnana', 'peAr', 'grApe'])
    assert actual.equals(expected), "str_replace failed"

def test_str_starts():
    """Can use str_starts"""
    df = tp.tibble(words = ['apple', 'bear', 'amazing'])
    actual = df.filter(tp.str_starts(col('words'), 'a'))
    expected = tp.tibble(words = ['apple', 'amazing'])
    assert actual.equals(expected), "str_starts failed"

def test_str_to_lower():
    """Can str_to_lower lowercase a string"""
    df = tp.tibble(name = ['APPLE', 'BANANA', 'PEAR', 'GRAPE'])
    actual = df.mutate(name = tp.str_to_lower(tp.col('name')))
    expected = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    assert actual.equals(expected), "str_to_lower failed"

def test_str_to_upper():
    """Can str_to_upper uppercase a string"""
    df = tp.tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(name = tp.str_to_upper(tp.col('name')))
    expected = tp.tibble(name = ['APPLE', 'BANANA', 'PEAR', 'GRAPE'])
    assert actual.equals(expected), "str_to_upper failed"

def test_str_trim():
    """Can str_to_upper uppercase a string"""
    df = tp.tibble(x = [' a ', ' b ', ' c '])
    actual = (
        df.mutate(both = tp.str_trim('x'),
                  left = tp.str_trim('x', "left"),
                  right = tp.str_trim('x', "right"))
        .drop('x')
    )
    expected = tp.tibble(
        both = ['a', 'b', 'c'],
        left = ['a ', 'b ', 'c '],
        right = [' a', ' b', ' c']
    )
    assert actual.equals(expected), "str_trim failed"