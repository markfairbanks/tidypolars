import tidypolars as tp
from tidypolars import col
import polars as pl
from tidypolars.utils import _repeat

def test_arrange1():
    """Can arrange ascending"""
    df = tp.Tibble(x = ['a', 'a', 'b'], y = [2, 1, 3])
    actual = df.arrange('y')
    expected = tp.Tibble(x = ['a', 'a', 'b'], y = [1, 2, 3])
    assert actual.frame_equal(expected), "arrange ascending failed"

def test_arrange2():
    """Can arrange descending"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.arrange(tp.desc('x'), 'y')
    expected = tp.Tibble({'x': ['b', 'a', 'a'], 'y': [3, 1, 2]})
    assert actual.frame_equal(expected), "arrange descending failed"

def test_bind_cols_single():
    """Can bind_cols"""
    df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3]})
    df2 = tp.Tibble({'z': [4, 4, 4]})
    actual = df1.bind_cols(df2)
    expected = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [1, 2, 3], 'z':[4, 4, 4]})
    assert actual.frame_equal(expected), "bind_cols failed"

def test_bind_cols_multiple():
    """Can bind_cols multiple"""
    df1 = tp.Tibble(x = range(3))
    df2 = tp.Tibble(y = range(3))
    df3 = tp.Tibble(z = range(3))
    actual = df1.bind_cols(df2, df3)
    expected = tp.Tibble(x = range(3), y = range(3), z = range(3))
    assert actual.frame_equal(expected), "multiple bind_cols failed"

def test_bind_rows_single():
    """Can bind rows"""
    df1 = tp.Tibble({'x': ['a', 'a'], 'y': [2, 1]})
    df2 = tp.Tibble({'x': ['b'], 'y': [3]})
    actual = df1.bind_rows(df2)
    expected = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    assert actual.frame_equal(expected), "bind_rows failed"

def test_bind_rows_auto_align():
    """Can bind rows"""
    df1 = tp.Tibble(x = ['a', 'a'], y = [2, 1])
    df2 = tp.Tibble(y = [3], x = ['b'])
    actual = df1.bind_rows(df2)
    expected = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    assert actual.frame_equal(expected), "bind_rows auto-align failed"

def test_bind_rows_multiple():
    """Can bind rows (multiple)"""
    df1 = tp.Tibble({'x': ['a', 'a'], 'y': [2, 1]})
    df2 = tp.Tibble({'x': ['b'], 'y': [3]})
    df3 = tp.Tibble({'x': ['b'], 'y': [3]})
    actual = df1.bind_rows(df2, df3)
    expected = tp.Tibble({'x': ['a', 'a', 'b', 'b'], 'y': [2, 1, 3, 3]})
    assert actual.frame_equal(expected), "bind_rows multiple failed"

def test_count_no_args():
    """Can count rows (no args)"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 1]})
    actual = df.count()
    expected = tp.Tibble({'n': [3]})
    assert actual.frame_equal(expected), "count with no args failed"

def test_count_one_arg():
    """Can count rows (one arg)"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 1]})
    actual = df.count('x', sort=True)
    expected = tp.Tibble({'x': ['a', 'b'], 'n': [2, 1]})
    assert actual.frame_equal(expected), "count with one arg failed"

def test_distinct_empty():
    """Can distinct columns"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': ['a', 'a', 'b']})
    actual = df.distinct()
    expected = tp.Tibble({'x': ['a', 'b'], 'y': ['a', 'b']})
    assert actual.frame_equal(expected), "empty distinct failed"

def test_distinct_select():
    """Can distinct columns"""
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': [2, 1, 3]})
    actual = df.distinct('x')
    expected = tp.Tibble({'x': ['a', 'b']})
    assert actual.frame_equal(expected), "distinct with select failed"

def test_drop():
    """Can drop columns"""
    df = tp.Tibble(x = range(3), y = range(3))
    actual = df.drop('x')
    expected = tp.Tibble(y = range(3))
    assert actual.frame_equal(expected), "drop failed"

def test_drop_null_empty():
    """Can drop nulls from all cols"""
    df = tp.Tibble(x = [1, None, 3], y = [None, 2, 3], z = range(1, 4))
    actual = df.drop_null()
    expected = tp.Tibble(x = [3], y = [3], z = [3])
    assert actual.frame_equal(expected), "empty drop_null failed"

def test_drop_null_select():
    """Can drop nulls with selection"""
    df = tp.Tibble(x = [1, None, 3], y = [None, 2, 3], z = range(1, 4))
    actual = df.drop_null('x')
    expected = tp.Tibble(x = [1, 3], y = [None, 3], z = [1, 3])
    assert actual.frame_equal(expected, null_equal = True), "drop_null with selection failed"

def test_fill():
    """Can fill"""
    df = tp.Tibble({'chr': ['a', None], 'int': [1, None]})
    actual = df.fill('chr', 'int')
    expected = tp.Tibble({'chr': ['a', 'a'], 'int': [1, 1]})
    assert actual.frame_equal(expected), "fill failed"

def test_filter():
    """Can filter multiple conditions"""
    df = tp.Tibble({'x': range(10), 'y': range(10)})
    actual = df.filter(col('x') <= 3, col('y') < 2)
    expected = tp.Tibble({'x': range(2), 'y': range(2)})
    assert actual.frame_equal(expected), "filter failed"

def test_full_join():
    """Can perform a full join"""
    df1 = tp.Tibble(x = ['a', 'a', 'b'], y = range(3))
    df2 = tp.Tibble(x = ['a'], z = range(1))
    actual = df1.full_join(df2)
    expected = tp.Tibble(y = [0, 1, 2], x = ['a', 'a', 'b'], z = [0, 0, None])
    assert actual.frame_equal(expected, null_equal = True), "full_join failed"

def test_inner_join():
    """Can perform a inner join"""
    df1 = tp.Tibble(x = ['a', 'a', 'b'], y = range(3))
    df2 = tp.Tibble(x = ['a'], z = range(1))
    actual = df1.inner_join(df2)
    expected = tp.Tibble(x = ['a', 'a'], y = [0, 1], z = [0, 0])
    assert actual.frame_equal(expected), "inner_join failed"

def test_left_join():
    """Can perform a left join"""
    df1 = tp.Tibble(x = ['a', 'a', 'b'], y = range(3))
    df2 = tp.Tibble(x = ['a', 'b'], z = range(2))
    actual = df1.left_join(df2)
    expected = tp.Tibble(x = ['a', 'a', 'b'], y = range(3), z = [0, 0 ,1])
    assert actual.frame_equal(expected), "left_join failed"

def test_mutate():
    """Can edit existing columns and can add columns"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    actual = df.mutate(double_x = col('x') * 2,
                       y = col('y') + 10)
    expected = tp.Tibble(
        {'x': _repeat(1, 3),
         'y': _repeat(12, 3),
          'double_x': _repeat(2, 3)}
    )
    assert actual.frame_equal(expected), "mutate failed"

def test_mutate_across():
    """Can mutate multiple columns simultaneously"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    actual = df.mutate(col(['x', 'y']) * 2,
                       x_plus_y = col('x') + col('y'))
    expected = tp.Tibble(
        {'x': _repeat(2, 3),
         'y': _repeat(4, 3),
         'x_plus_y': _repeat(3, 3)}
    )
    assert actual.frame_equal(expected), "mutate across failed"

def test_names():
    """Can get column names"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    assert df.names == ['x', 'y'], "names failed"

def test_ncol():
    """Can number of columns"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    assert df.ncol == 2, "ncol failed"

def test_nrow():
    """Can number of rows"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    assert df.nrow == 3, "nrow failed"

def test_pivot_longer1():
    "Can pivot all (unspecified) cols to long"
    df = tp.Tibble({'x': [1, 2], 'y': [3, 4]})
    actual = df.pivot_longer()
    expected = tp.Tibble({'name': ['x', 'x', 'y', 'y'], 'value': range(1, 5)})
    assert actual.frame_equal(expected), "unspecified pivot_longer failed"

def test_pivot_longer2():
    """Can pivot all (specified) cols to long"""
    df = tp.Tibble({'x': [1, 2], 'y': [3, 4]})
    actual = df.pivot_longer(['x', 'y'])
    expected = tp.Tibble({'name': ['x', 'x', 'y', 'y'], 'value': range(1, 5)})
    assert actual.frame_equal(expected), "specified pivot_longer failed"

def test_pivot_wider1():
    """Can pivot all cols to wide"""
    df = tp.Tibble({'label': ['x', 'y', 'z'], 'val': range(1, 4)})
    actual = df.pivot_wider(names_from = 'label', values_from = 'val').select('x', 'y', 'z')
    expected = tp.Tibble({'x': [1], 'y': [2], 'z': [3]})
    assert actual.frame_equal(expected), "pivot_wider all cols failed"

def test_pivot_wider2():
    """Can pivot cols to wide with id col"""
    df = tp.Tibble({'id': _repeat(1, 3), 'label': ['x', 'y', 'z'], 'val': range(1, 4)})
    actual = df.pivot_wider(names_from = 'label', values_from = 'val').select('id', 'x', 'y', 'z')
    expected = tp.Tibble({'id': [1], 'x': [1], 'y': [2], 'z': [3]})
    assert actual.frame_equal(expected), "pivot_wider with id failed"

def test_pivot_wider3():
    """Can pivot cols to wide with values filled"""
    df = tp.Tibble({'id': _repeat(1, 3), 'label': ['x', 'y', 'z'], 'val': range(1, 4)})
    actual = (
        df.pivot_wider(names_from = 'label', values_from = 'id', values_fill = 0)
        .select('val', 'x', 'y', 'z').arrange('val')
    )
    expected = tp.Tibble({'val': [1, 2, 3], 'x': [1, 0, 0], 'y': [0, 1, 0], 'z': [0, 0, 1]})
    assert actual.frame_equal(expected), "pivot_wider with values filled failed"

def test_pivot_wider4():
    """Can pivot cols to wide with values filled - doesn't affect id col"""
    df = tp.Tibble(id = [None, 2], var = ["x", "y"], val = [1, 2])
    actual = (
        df.pivot_wider(names_from = "var", values_from = "val", values_fill = 0)
        .select('id', 'x', 'y')
        .arrange('y')
    )
    expected = tp.Tibble({'id': [None, 2], 'x': [1, 0], 'y': [0, 2]})
    assert actual.frame_equal(expected), "pivot_wider with values filled failed"

def test_print():
    """Printing doesn't alter class of df"""
    df = tp.Tibble(x = range(3), y = range(3))
    repr(df)
    print(df)
    assert isinstance(df, tp.Tibble), "Printing failed"

def test_pull():
    """Can use pull"""
    df = tp.Tibble({'x': _repeat(1, 3), 'y': _repeat(2, 3)})
    actual = df.pull('x')
    expected = df.to_polars().get_column('x')
    assert actual == expected, "pull failed"

def test_relocate_before():
    """Can relocate before columns"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.relocate('y', 'z', before = 'x')
    expected = df.select('y', 'z', 'x')
    assert actual.frame_equal(expected), "relocate before failed"

def test_relocate_after():
    """Can relocate after columns"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.relocate('z', 'y', after = 'x')
    expected = df.select('x', 'z', 'y')
    assert actual.frame_equal(expected), "relocate after failed"

def test_relocate_empty():
    """Can relocate to the beginning"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.relocate('z', 'y')
    expected = df.select('z', 'y', 'x')
    assert actual.frame_equal(expected), "relocate to the beginning failed"

def test_rename_dplyr_kwargs():
    """Can rename - dplyr interface (kwargs)"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.rename(new_x = 'x', new_y = 'y')
    expected = tp.Tibble({'new_x': range(3), 'new_y': range(3), 'z': range(3)})
    assert actual.frame_equal(expected), "dplyr rename failed"

def test_rename_dplyr_strings():
    """Can rename - dplyr interface (strings)"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.rename('new_x', 'x', 'new_y', 'y')
    expected = tp.Tibble({'new_x': range(3), 'new_y': range(3), 'z': range(3)})
    assert actual.frame_equal(expected), "dplyr rename failed"

def test_rename_pandas():
    """Can rename - pandas interface"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.rename({'x': 'new_x', 'y': 'new_y'})
    expected = tp.Tibble({'new_x': range(3), 'new_y': range(3), 'z': range(3)})
    assert actual.frame_equal(expected), "pandas rename failed"

def test_replace_null():
    """Can replace nulls"""
    df = tp.Tibble(x = [0, None], y = [None, None])
    actual = df.replace_null(dict(x = 1, y = 2))
    expected = tp.Tibble(x = [0, 1], y = [2, 2])
    assert actual.frame_equal(expected), "replace_null method failed"

def test_set_names():
    """Can set_names"""
    df = tp.Tibble(x = range(3), y = range(3))
    actual = df.set_names(['a', 'b'])
    expected = tp.Tibble(a = range(3), b = range(3))
    assert actual.frame_equal(expected), "set_names failed"

def test_select():
    """Can select columns"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.select('x', 'z')
    expected = df[['x', 'z']]
    assert actual.frame_equal(expected), "select failed"

def test_slice():
    """Can slice"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice(0, 2)
    expected = tp.Tibble({'x': [0, 2], 'y': ['a', 'b']})
    assert actual.frame_equal(expected), "slice failed"

def test_slice_head():
    """Can slice_head"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice_head(2)
    expected = tp.Tibble({'x': [0, 1], 'y': ['a', 'a']})
    assert actual.frame_equal(expected), "slice_head failed"

def test_slice_tail():
    """Can slice_tail by group"""
    df = tp.Tibble({'x': range(3), 'y': ['a', 'a', 'b']})
    actual = df.slice_tail(2)
    expected = tp.Tibble({'x': [1, 2], 'y': ['a', 'b']})
    assert actual.frame_equal(expected), "slice_tail failed"

def test_summarise():
    """Can use summarise alias"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.summarise(avg_x = col('x').mean())
    expected = tp.Tibble({'avg_x': [1]})
    assert actual.frame_equal(expected), "summarise failed"

def test_summarize():
    """Can use summarize"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    actual = df.summarize(avg_x = col('x').mean())
    expected = tp.Tibble({'avg_x': [1]})
    assert actual.frame_equal(expected), "ungrouped summarize failed"

def test_summarize_grouped():
    """Can use summarize by group"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': ['a', 'a', 'b']})
    actual = df.summarize(avg_x = col('x').mean(), by = 'z').arrange('z')
    expected = tp.Tibble(z = ['a', 'b'], avg_x = [.5, 2])
    assert actual.frame_equal(expected), "grouped summarize failed"

def test_summarize_across():
    """Can use summarize_across"""
    df = tp.Tibble(x = range(3), y = range(3), z = range(3))
    actual = df.summarize(col(['x', 'y']).max().prefix('max_'),
                          avg_x = col('x').mean())
    expected = tp.Tibble({'max_x': [2], 'max_y': [2], 'avg_x': [1]})
    assert actual.frame_equal(expected), "ungrouped summarize across failed"

def test_to_dict():
    """Can convert to a dictionary"""
    df = tp.Tibble({'x': range(3), 'y': range(3)})
    assert df.to_dict() == {'x': pl.Series(range(3)), 'y': pl.Series(range(3))}
    assert df.to_dict() == {'x': list(range(3)), 'y': list(range(3))}

def test_to_polars():
    """Can convert to a polars DataFrame"""
    df = tp.Tibble({'x': range(3), 'y': range(3), 'z': range(3)})
    assert isinstance(df.to_polars(), pl.DataFrame), "to_polars failed"

def test_funs_in_a_row():
    df = tp.Tibble(x = range(3), y = range(3), z = range(3))
    df.distinct()
    df.drop('x')
    df.drop_null()
    df.filter(col('x') < 7)
    df.head()
    df.mutate(col('x') * 2)
    df.relocate('y', before = 'x')
    df.rename({'x': 'new_x'})
    df.select('x', 'y')
    df.slice(1)
    df.slice_head()
    df.slice_tail()
    df.tail()
    df.arrange('x', 'y')
    assert True, "Functions in a row failed"
