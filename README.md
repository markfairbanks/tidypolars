# tidypolars

tidypolars is a data frame library built on top of the blazingly fast [polars](https://github.com/pola-rs/polars) library that gives access to methods and function familiar to R tidyverse users.

## Installation
```bash
$ pip3 install tidypolars
```

## Usage

```python
import tidypolars as tp
from tidypolars import col

test_df = tp.tidyframe({'x': range(3), 'y': range(4, 7), 'z': ['a', 'a', 'b']})

(
    test_df
    .select('x', 'y', 'z')
    .filter(col('x') < 4, col('y') > 1)
    .arrange('x', 'y')
    .mutate(double_x = col('x') * 2,
            x_plus_y = col('x') + col('y'))
)
shape: (3, 5)
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

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`tidypolars` was created by Mark Fairbanks. It is licensed under the terms of the MIT license.

## Credits

`tidypolars` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
