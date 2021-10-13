# Changelog

## v0.1.7 (in development)
* New Tibble methods
  + `.drop_null()`

* New functions
  + `tp.case_when()`
  + `tp.if_else()`

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

* New expression methods
  + `.lag()`
  + `.lead()`

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