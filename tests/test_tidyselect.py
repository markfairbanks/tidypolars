import tidypolars as tp

def test_contains_ignore_case():
    """Can find columns that contain and ignores case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.contains('M', True))
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.equals(expected), "contains ignore case failed"

def test_contains_include_case():
    """Can find columns that contain and includes case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.contains('M', ignore_case=False))
    expected = tp.Tibble({'NUMBER': [2, 1, 1]})
    assert actual.equals(expected), "contains includes case failed"

def test_ends_with_ignore_case():
    """Can find columns that ends_with and ignores case"""
    df = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.ends_with('er', True))
    expected = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.equals(expected), "ends_with ignore case failed"

def test_ends_with_include_case():
    """Can find columns that ends_with and ignores case"""
    df = tp.Tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.ends_with('er', ignore_case=False))
    expected = tp.Tibble({'writer': ['a', 'a', 'b']})
    assert actual.equals(expected), "ends_with ignore case failed"

def test_everything():
    """Can find all columns"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    actual = df.select(tp.everything())
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    assert actual.equals(expected), "everything failed"

def test_starts_with_ignore_case():
    """Can find columns that starts_with and ignores case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.starts_with('n', True))
    expected = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    assert actual.equals(expected), "starts_with ignore case failed"

def test_starts_with_include_case():
    """Can find columns that starts_with and includes case"""
    df = tp.Tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.starts_with('n', ignore_case=False))
    expected = tp.Tibble({'name': ['a', 'a', 'b']})
    assert actual.equals(expected), "starts_with include case failed"