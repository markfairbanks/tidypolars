# Changelog

## v0.2.9

### Bug fixes
* Update `.distinct()` to work with polars >= 0.12.20

## v0.2.8 (2021/12/08)

#### Bug fixes
* Can use `fmt` arg in `as_date()` and `as_datetime()` (#155)

## v0.2.7 (2021/11/19)

#### New Tibble methods
* `.to_dict()`

## v0.2.6 (2021/11/18)

#### New functions

* `count()`
* `floor()`
* `length()`
* `quantile()`
* `sqrt()`

#### Functionality improvements

* `.bind_rows()`: Auto-aligns columns by name

## v0.2.5 (2021/11/16)

## v0.2.4 (2021/11/15)

## v0.2.3 (2021/11/15)

## v0.2.2 (2021/11/15)

#### New functions
* `paste()`
* `paste0()`

#### Improved functionality

* `.relocate()`: tidyselect helpers work

## v0.2.1 (2021/11/08)

#### New Tibble methods

* `.replace_null()`
* `.set_names()`

#### New functions

* `replace_null()`

## v0.2.0 (2021/11/05)

#### New Functions

* `as_float()`
* `as_integer()`
* `as_string()`
* `between()`
* `cast()`
* `desc()`
* `is_finite()`
* `is_in()`
* `is_infinite()`
* `is_not()`
* `is_not_in()`
* `is_not_null()`
* `is_null()`
* `round()`
* `lubridate`
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
  * `week()`
  * `yday()`
  * `year()`
* `stringr`
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

#### Improved functionality

* `.drop()`: tidyselect helpers work

## v0.1.7 (2021/10/20)

#### New Tibble methods

* `.count()`
* `.drop_null()`
* `.inner_join()`/`.left_join()`/`.full_join()`
* `.frame_equal()`
* `.write_csv()`
* `.write_parquet()`

#### New functions

* `abs()`
* `case_when()`
* `first()`
* `if_else()`
* `lag()`
* `last()`
* `lead()`
* `max()`
* `mean()`
* `median()`
* `min()`
* `n_distinct()`
* `read_csv()`
* `read_parquet()`
* `sd()`
* `sum()`
* `tidyselect`
  * `contains()`
  * `ends_with()`
  * `everything()`
  * `starts_with()`

#### Improved functionality

* `.bind_cols()`/`.bind_rows()`: Can append multiple data frames in one call

## v0.1.6 (2021/10/13)

#### Improved functionality

* `.rename()`: Can now use both a dplyr-like and pandas-like interface
  
#### New attributes
* `.names`
* `.ncol`
* `.nrow`

## v0.1.5 (2021/10/12)

#### New Tibble methods

* `.fill()`
* `.head()`
* `.pivot_longer()`
* `.pivot_wider()`
* `.tail()`
* `.slice_head()`
* `.slice_tail()`

## v0.1.4 (2021/10/06)

#### New Tibble methods

* `.bind_cols()`
* `.bind_rows()`
* `.distinct()`
* `.pull()`
* `.rename()`
* `.slice()`

#### Methods with new `by` arg

* `.filter()`
* `.mutate()`
* `.slice()`
* `.summarize()`

#### Miscellaneous

* Class name changed from tibble to Tibble

## v0.1.3 (2021/10/04)

* Class name changed from tidyframe to tibble

## v0.1.2 (2021/10/04)

## v0.1.1 (2021/10/04)

## v0.1.0 (2021/10/02)

* First release of `tidypolars`