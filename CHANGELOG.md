# Changelog

## v0.1.8 (in development)
#### New Functions
* `between()`
* `is_finite()`
* `is_in()`
* `is_infinite()`
* `is_not()`
* `is_not_in()`
* `is_not_null()`
* `is_null()`
* `round()`
* `stringr`
  + `.str_detect()`
  + `.str_length()`
  + `.str_remove_all()`
  + `.str_remove()`
  + `.str_replace_all()`
  + `.str_replace()`
  + `.str_sub()`
  + `.str_to_lower()`
  + `.str_to_upper()`

## v0.1.7 (2021/10/20)
#### New Tibble methods
* `.count()`
* `.drop_null()`
* `.inner_join()`/`.left_join()`/`.outer_join()`
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
  + `col_contains()`
  + `col_ends_with()`
  + `col_everything()`
  + `col_starts_with()`

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

#### Methods with new `groupby` arg:
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