import tidypolars as tp

def test_contains_ignore_case():
    """Can find columns that contain and ignores case"""
    df = tp.tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.contains('M', True))
    expected = tp.tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.equals(expected), "contains ignore case failed"

def test_contains_include_case():
    """Can find columns that contain and includes case"""
    df = tp.tibble({'name': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.contains('M', ignore_case=False))
    expected = tp.tibble({'NUMBER': [2, 1, 1]})
    assert actual.equals(expected), "contains includes case failed"

def test_ends_with_ignore_case():
    """Can find columns that ends_with and ignores case"""
    df = tp.tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.ends_with('er', True))
    expected = tp.tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    assert actual.equals(expected), "ends_with ignore case failed"

def test_ends_with_include_case():
    """Can find columns that ends_with and ignores case"""
    df = tp.tibble({'writer': ['a', 'a', 'b'], 'NUMBER': [2, 1, 1]})
    actual = df.select(tp.ends_with('er', ignore_case=False))
    expected = tp.tibble({'writer': ['a', 'a', 'b']})
    assert actual.equals(expected), "ends_with ignore case failed"

def test_everything():
    """Can find all columns"""
    df = tp.tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    actual = df.select(tp.everything())
    expected = tp.tibble({'name': ['a', 'a', 'b'], 'value': [2, 1, 1]})
    assert actual.equals(expected), "everything failed"

def test_starts_with_ignore_case():
    """Can find columns that starts_with and ignores case"""
    df = tp.tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.starts_with('n', True))
    expected = tp.tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    assert actual.equals(expected), "starts_with ignore case failed"

def test_starts_with_include_case():
    """Can find columns that starts_with and includes case"""
    df = tp.tibble({'name': ['a', 'a', 'b'], 'Number': [2, 1, 1]})
    actual = df.select(tp.starts_with('n', ignore_case=False))
    expected = tp.tibble({'name': ['a', 'a', 'b']})
    assert actual.equals(expected), "starts_with include case failed"

def test_where():
    """Can use where"""
    df = tp.tibble({
        "string_col": ["a"],
        "numeric_col": [1]
    })
    actual = df.select(tp.where("string"))
    expected = df.select("string_col")
    assert actual.equals(expected), "where('numeric') failed"
    actual = df.select(tp.where("numeric"))
    expected = df.select("numeric_col")
    assert actual.equals(expected), "where('numeric') failed"