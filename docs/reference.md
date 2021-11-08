# Reference

## Tibble methods

#### dplyr

* [`.arrange()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.arrange)
* [`.bind_cols()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.bind_cols)
* [`.bind_rows()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.bind_rows)
* [`.count()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.count)
* [`.distinct()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.distinct)
* [`.drop()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.drop)
* [`.head()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.head)
* [`.filter()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.filter)
* Joins
  * [`.full_join()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.full_join)
  * [`.inner_join()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.inner_join)
  * [`.left_join()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.left_join)
* [`.pull()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.pull)
* [`.relocate()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.relocate)
* [`.slice()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.slice)
* [`.slice_head()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.slice_head)
* [`.slice_tail()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.slice_tail)
* [`.summarize()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.summarize)
* [`.tail()`](https://tidypolars.readthedocs.io/en/latest/autoapi/tidypolars/tidypolars/index.html#tidypolars.tidypolars.Tibble.tail)

#### tidyr

* `.drop_null()`
* `.fill()`
* `.pivot_longer()`
* `.pivot_wider()`


## Functions

#### General functions

* `abs()`
* `as_float()`
* `as_integer()`
* `as_string()`
* `between()`
* `case_when()`
* `cast()`
* `first()`
* `if_else()`
* `is_finite()`
* `is_in()`
* `is_infinite()`
* `is_nan()`
* `is_not()`
* `is_not_in()`
* `is_not_null()`
* `is_null()`
* `lag()`
* `last()`
* `lead()`
* `max()`
* `mean()`
* `median()`
* `min()`
* `n_distinct()`
* `sd()`
* `sum()`

#### lubridate

* `as_date()`
* `as_datetime()`
* `dt_round()`
* `hour()`
* `mday()`
* `minute()`
* `month()`
* `quarter()`
* `second()`
* `wday()`
* `yday()`
* `year()`

#### stringr

* `str_detect()`
* `str_extract()`
* `str_length()`
* `str_remove_all()`
* `str_remove()`
* `str_replace_all()`
* `str_replace()`
* `str_sub()`
* `str_to_lower()`
* `str_to_upper()`
* `str_trim()`

#### tidyselect
* `contains()`
* `ends_with()`
* `everything()`
* `starts_with()`

## Converting from/to pandas DataFrame

* `from_pandas()`
* `.to_pandas()`

## Reading/writing data

#### Tibble Methods

* `.write_csv()`
* `.write_parquet()`

#### Functions

* `read_csv()`
* `.read_parquet()`