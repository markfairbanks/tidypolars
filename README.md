# tidypolars
[![PyPI Latest Release](https://img.shields.io/pypi/v/tidypolars.svg)](https://pypi.org/project/tidypolars/)
[![conda-forge](https://anaconda.org/conda-forge/tidypolars/badges/version.svg)](https://anaconda.org/conda-forge/tidypolars)

tidypolars is a data frame library built on top of the blazingly fast [polars](https://github.com/pola-rs/polars) library that gives access to methods and functions familiar to R tidyverse users.

## Installation
You can install tidypolars with `pip`:

```bash
$ pip install tidypolars
```

Or through `conda`:
```bash
$ conda install -c conda-forge tidypolars
```

### General syntax

tidypolars methods are designed to work like tidyverse functions:

```python
import tidypolars as tp
from tidypolars import col, desc

df = tp.tibble(x = range(3), y = range(3, 6), z = ['a', 'a', 'b'])

(
    df
    .select('x', 'y', 'z')
    .filter(col('x') < 4, col('y') > 1)
    .arrange(desc('z'), 'x')
    .mutate(double_x = col('x') * 2,
            x_plus_y = col('x') + col('y'))
)
┌─────┬─────┬─────┬──────────┬──────────┐
│ x   ┆ y   ┆ z   ┆ double_x ┆ x_plus_y │
│ --- ┆ --- ┆ --- ┆ ---      ┆ ---      │
│ i64 ┆ i64 ┆ str ┆ i64      ┆ i64      │
╞═════╪═════╪═════╪══════════╪══════════╡
│ 2   ┆ 5   ┆ b   ┆ 4        ┆ 7        │
├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 0   ┆ 3   ┆ a   ┆ 0        ┆ 3        │
├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ 4   ┆ a   ┆ 2        ┆ 5        │
└─────┴─────┴─────┴──────────┴──────────┘
```

The key difference from R is that column names must be wrapped in `col()` in the following methods:
* `.filter()`
* `.mutate()`
* `.summarize()`

The general idea - when doing calculations on a column you need to wrap it in `col()`. When doing simple column selections (like in `.select()`) you can pass the column names as strings.

A full list of functions can be found [here](https://tidypolars.readthedocs.io/en/latest/reference.html).

### Group by syntax

Methods operate by group by calling the `by` arg.

* A single column can be passed with `_by = 'z'`
* Multiple columns can be passed with `_by = ['y', 'z']`

```python
(
    df
    .summarize(avg_x = tp.mean(col('x')),
               _by = 'z')
)
┌─────┬───────┐
│ z   ┆ avg_x │
│ --- ┆ ---   │
│ str ┆ f64   │
╞═════╪═══════╡
│ a   ┆ 0.5   │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ b   ┆ 2     │
└─────┴───────┘
```

### Selecting/dropping columns

tidyselect functions can be mixed with normal selection when selecting columns:

```python
df = tp.tibble(x1 = range(3), x2 = range(3), y = range(3), z = range(3))

df.select(tp.starts_with('x'), 'z')
┌─────┬─────┬─────┐
│ x1  ┆ x2  ┆ z   │
│ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╡
│ 0   ┆ 0   ┆ 0   │
├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 1   ┆ 1   ┆ 1   │
├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┤
│ 2   ┆ 2   ┆ 2   │
└─────┴─────┴─────┘
```

To drop columns use the `.drop()` method:

```python
df.drop(tp.starts_with('x'), 'z')
┌─────┐
│ y   │
│ --- │
│ i64 │
╞═════╡
│ 0   │
├╌╌╌╌╌┤
│ 1   │
├╌╌╌╌╌┤
│ 2   │
└─────┘
```

### Converting to/from pandas data frames

If you need to use a package that requires pandas data frames, you can convert from a tidypolars `Tibble` to
a pandas `DataFrame`.

To do this you'll first need to install pyarrow:

```bash
pip install pyarrow
```

To convert to a pandas `DataFrame`:

```python
df = df.as_pandas()
```

To convert from a pandas `DataFrame` to a tidypolars `tibble`:

```python
df = tp.as_tibble(df)
```

## Speed Comparisons

A few notes:

* Comparing times from separate functions typically isn't very useful. For example - the `.summarize()` tests
  were performed on a different dataset from `.pivot_wider()`.
* All tests are run 5 times. The times shown are the median of those 5 runs.
* All timings are in milliseconds.
* All tests can be found in the source code 
  [here](https://github.com/markfairbanks/tidypolars/blob/main/benchmarks/benchmarks.ipynb).
* FAQ - Why are some `tidypolars` functions faster than their `polars` counterpart?
  + Short answer - they're not! After all they're just using `polars` in the background.
  + Long answer - All python functions have some slight natural variation in their execution time. 
  By chance the `tidypolars` runs were slightly shorter on those specific functions on this
  iteration of the tests. However one goal of these tests is to show that the "time cost" of
  translating syntax to `polars` is very negligible to the
  user (especially on medium-to-large datasets).
* Lastly I'd like to mention that these tests were not rigorously created to cover all angles equally. They are just meant to be used as general insight into the performance of these packages.

```python
┌─────────────┬────────────┬─────────┬──────────┐
│ func_tested ┆ tidypolars ┆ polars  ┆ pandas   │
│ ---         ┆ ---        ┆ ---     ┆ ---      │
│ str         ┆ f64        ┆ f64     ┆ f64      │
╞═════════════╪════════════╪═════════╪══════════╡
│ arrange     ┆ 752.298    ┆ 750.386 ┆ 768.677  │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ case_when   ┆ 134.716    ┆ 135.721 ┆ 84.105   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ distinct    ┆ 40.683     ┆ 42.03   ┆ 270.724  │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ filter      ┆ 30.346     ┆ 30.163  ┆ 216.383  │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ left_join   ┆ 889.414    ┆ 900.966 ┆ 2723.635 │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ mutate      ┆ 15.976     ┆ 8.513   ┆ 78.746   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ pivot_wider ┆ 40.915     ┆ 42.768  ┆ 144.66   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ summarize   ┆ 78.795     ┆ 68.275  ┆ 300.896  │
└─────────────┴────────────┴─────────┴──────────┘
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.
