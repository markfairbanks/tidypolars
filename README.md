# tidypolars

tidypolars is a data frame library built on top of the blazingly fast [polars](https://github.com/pola-rs/polars) library that gives access to methods and functions familiar to R tidyverse users.

## Installation
```bash
$ pip3 install tidypolars
```

## Usage

```python
import tidypolars as tp
from tidypolars import col

test_df = tp.Tibble(x = range(3), y = range(4, 7), z = ['a', 'a', 'b'])

(
    test_df
    .select('x', 'y', 'z')
    .filter(col('x') < 4, col('y') > 1)
    .arrange('x', 'y')
    .mutate(double_x = col('x') * 2,
            x_plus_y = col('x') + col('y'))
)
┌─────┬─────┬─────┬──────────┬──────────┐
│ x   ┆ y   ┆ z   ┆ double_x ┆ x_plus_y │
│ --- ┆ --- ┆ --- ┆ ---      ┆ ---      │
│ i64 ┆ i64 ┆ str ┆ i64      ┆ i64      │
╞═════╪═════╪═════╪══════════╪══════════╡
│ 0   ┆ 4   ┆ "a" ┆ 0        ┆ 4        │
├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 1   ┆ 5   ┆ "a" ┆ 2        ┆ 6        │
├╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ 2   ┆ 6   ┆ "b" ┆ 4        ┆ 8        │
└─────┴─────┴─────┴──────────┴──────────┘
```


### Using `by`

Methods operate by group by calling the `by` arg.

* A single column can be passed with `by = 'z'`
* Multiple columns can be passed with `by = ['y', 'z']`

```python
(
    test_df
    .summarize(avg_x = tp.mean(col('x')),
               by = 'z')
)
┌─────┬───────┐
│ z   ┆ avg_x │
│ --- ┆ ---   │
│ str ┆ f64   │
╞═════╪═══════╡
│ "b" ┆ 2     │
├╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ "a" ┆ 0.5   │
└─────┴───────┘
```

## Speed Comparisons

```python
┌─────────────┬────────────┬─────────┬──────────┐
│ func_tested ┆ tidypolars ┆ polars  ┆ pandas   │
│ ---         ┆ ---        ┆ ---     ┆ ---      │
│ str         ┆ f64        ┆ f64     ┆ f64      │
╞═════════════╪════════════╪═════════╪══════════╡
│ arrange     ┆ 190.345    ┆ 169.478 ┆ 500.112  │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ case_when   ┆ 87.348     ┆ 79.427  ┆ 152.623  │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ distinct    ┆ 16.888     ┆ 16.282  ┆ 28.725   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ filter      ┆ 29.789     ┆ 29.91   ┆ 231.397  │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ full_join   ┆ 236.784    ┆ 231.283 ┆ 1042.689 │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ inner_join  ┆ 49.71      ┆ 47.563  ┆ 630.98   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ left_join   ┆ 113.792    ┆ 115     ┆ 1100.607 │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ mutate      ┆ 7.979      ┆ 7.408   ┆ 117.283  │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ pivot_wider ┆ 42.764     ┆ 39.939  ┆ 49.048   │
├╌╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌┤
│ summarize   ┆ 59.434     ┆ 58.011  ┆ 453.707  │
└─────────────┴────────────┴─────────┴──────────┘
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`tidypolars` was created by Mark Fairbanks. It is licensed under the terms of the MIT license.

## Credits

`tidypolars` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
