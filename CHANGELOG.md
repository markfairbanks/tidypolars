# Changelog

## v0.1.7 (2021/10/20)
* New Tibble methods
  + `.count()`
  + `.drop_null()`
  + `.inner_join()`/`.left_join()`/`.outer_join()`
  + `.write_csv()`
  + `.write_parquet()`

* New functions
  + `tp.abs()`
  + `tp.case_when()`
  + `tp.first()`
  + `tp.if_else()`
  + `tp.lag()`
  + `tp.last()`
  + `tp.lead()`
  + `tp.max()`
  + `tp.mean()`
  + `tp.median()`
  + `tp.min()`
  + `tp.n_distinct()`
  + `tp.sd()`
  + `tp.sum()`
  + `tp.read_csv()`
  + `tp.read_parquet()`
  + tidyselect
    - `tp.contains()`
    - `tp.ends_with()`
    - `tp.everything()`
    - `tp.starts_with()`

* Improved functionality
  + `.bind_cols()`/`.bind_rows()`: Can append multiple data frames in one call

## v0.1.6 (2021/10/13)
* Improved functionality
  + `.rename()`: Can now use both a dplyr-like and pandas-like interface
  
* New attributes
  + `.names`
  + `.ncol`
  + `.nrow`

## v0.1.5 (2021/10/12)
* New Tibble methods
  + `.fill()`
  + `.head()`
  + `.pivot_longer()`
  + `.pivot_wider()`
  + `.tail()`
  + `.slice_head()`
  + `.slice_tail()`

## v0.1.4 (2021/10/06)
* New Tibble methods
  + `.bind_cols()`
  + `.bind_rows()`
  + `.distinct()`
  + `.pull()`
  + `.rename()`
  + `.slice()`

* Methods with new `groupby` arg:
  + `.filter()`
  + `.mutate()`
  + `.slice()`
  + `.summarize()`

* Class name changed from tibble to Tibble

## v0.1.3 (2021/10/04)

* Class name changed from tidyframe to tibble

## v0.1.2 (2021/10/04)

## v0.1.1 (2021/10/04)

## v0.1.0 (2021/10/02)

* First release of `tidypolars`