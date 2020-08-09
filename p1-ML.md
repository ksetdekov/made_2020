---
title: "classification"
author: "Kirill Setdekov"
date: "09 08 2020"
output:
  html_document:
    keep_md: yes
---



## import

```r
library(readr)
train <- read_csv("data/train.csv", col_names = FALSE)
```

```
## Parsed with column specification:
## cols(
##   .default = col_double()
## )
```

```
## See spec(...) for full column specifications.
```

```r
View(train)
```

