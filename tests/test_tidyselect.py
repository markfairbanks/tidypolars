import tidypolars as tp
# ADD TP to all selects
def _repeat(x, times):
    if not isinstance(x, list):
        x = [x]
    return x * times

def test_contains_ignore_case():
    """Can find columns that contain and ignores case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.contains('M'))
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.frame_equal(expected), "contains ignore case failed"

def test_contains_include_case():
    """Can find columns that contain and includes case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.contains('M', ignorecase=False))
    expected = tp.Tibble({'NUMBER': [2, 1, 1]})
    assert actual.frame_equal(expected), "contains includes case failed"

def test_ends_with_ignore_case():
    """Can find columns that ends_with and ignores case"""
    df = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.ends_with('er'))
    expected = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.frame_equal(expected), "ends_with ignore case failed"

def test_ends_with_include_case():
    """Can find columns that ends_with and ignores case"""
    df = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.ends_with('er', ignorecase=False))
    expected = tp.Tibble({'writer': ['a', 'a', 'b']})
    assert actual.frame_equal(expected), "ends_with ignore case failed"

def test_everything():
    """Can find all columns"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    actual = df.select(tp.everything())
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    assert actual.frame_equal(expected), "everything failed"

def test_starts_with_ignore_case():
    """Can find columns that starts_with and ignores case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.starts_with('n'))
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    assert actual.frame_equal(expected), "starts_with ignore case failed"

def test_starts_with_include_case():
    """Can find columns that starts_with and includes case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.starts_with('n', ignorecase=False))
    expected = tp.Tibble({'name': ['a', 'a', 'b']})
    assert actual.frame_equal(expected), "starts_with include case failed"