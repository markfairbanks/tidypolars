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
```

```
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
```

```
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
```

```
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
```

```
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

If you need to use a package that requires pandas data frames, you can convert from a tidypolars `tibble` to
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

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.
