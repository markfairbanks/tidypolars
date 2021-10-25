import tidypolars as tp
# ADD TP to all selects
def _repeat(x, times):
    if not isinstance(x, list):
        x = [x]
    return x * times

def test_col_contains_ignore_case():
    """Can find columns that contain and ignores case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.col_contains('M'))
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.frame_equal(expected), "col_contains ignore case failed"

def test_col_contains_include_case():
    """Can find columns that contain and includes case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.col_contains('M', ignore_case=False))
    expected = tp.Tibble({'NUMBER': [2, 1, 1]})
    assert actual.frame_equal(expected), "col_contains includes case failed"

def test_col_ends_with_ignore_case():
    """Can find columns that col_ends_with and ignores case"""
    df = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.col_ends_with('er'))
    expected = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.frame_equal(expected), "col_ends_with ignore case failed"

def test_col_ends_with_include_case():
    """Can find columns that col_ends_with and ignores case"""
    df = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.col_ends_with('er', ignore_case=False))
    expected = tp.Tibble({'writer': ['a', 'a', 'b']})
    assert actual.frame_equal(expected), "col_ends_with ignore case failed"

def test_col_everything():
    """Can find all columns"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    actual = df.select(tp.col_everything())
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    assert actual.frame_equal(expected), "col_everything failed"

def test_col_starts_with_ignore_case():
    """Can find columns that col_starts_with and ignores case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.col_starts_with('n'))
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    assert actual.frame_equal(expected), "col_starts_with ignore case failed"

def test_col_starts_with_include_case():
    """Can find columns that col_starts_with and includes case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.col_starts_with('n', ignore_case=False))
    expected = tp.Tibble({'name': ['a', 'a', 'b']})
    assert actual.frame_equal(expected), "col_starts_with include case failed"