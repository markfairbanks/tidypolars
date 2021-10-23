import tidypolars as tp
# ADD TP to all selects
def _repeat(x, times):
    if not isinstance(x, list):
        x = [x]
    return x * times

def test_str_detect_single():
    """Can str_detect find a single string"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(single = tp.str_detect('name', ['a']), single_negate = tp.str_detect('name', ['a'], negate=True))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                         single = [True, True, True, True], 
                         single_negate = [False, False, False, False]
                         )
    assert actual.frame_equal(expected), "str_detect single failed"

def test_str_detect_multiple():
    """Can str_detect find multiple strings"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(multiple = tp.str_detect('name', ['a', 'e']), multiple_negate = tp.str_detect('name', ['a', 'e'], negate=True))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'], 
                        multiple = [True, False, True, True], 
                        multiple_negate = [False, True, False, False])
    assert actual.frame_equal(expected), "str_detect multiple failed"

def test_str_to_upper():
    """Can str_to_upper uppercase a string"""
    df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    actual = df.mutate(name = tp.str_to_upper(tp.col('name')))
    expected = tp.Tibble(name = ['APPLE', 'BANANA', 'PEAR', 'GRAPE'])
    assert actual.frame_equal(expected), "str_to_upper multiple failed"

def test_str_to_lower():
    """Can str_to_lower lowercase a string"""
    df = tp.Tibble(name = ['APPLE', 'BANANA', 'PEAR', 'GRAPE'])
    actual = df.mutate(name = tp.str_to_lower(tp.col('name')))
    expected = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    assert actual.frame_equal(expected), "str_to_lower multiple failed"