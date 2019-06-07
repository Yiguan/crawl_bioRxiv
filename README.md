A Python crawler to get some information about bioRxiv, including the titles and the dates of papers in bioRxiv.

1. Using Python download:

  Packages used in Python script:
  ```{python}
  from Cookie2Dict import cookie2dict
  import requests
  import re
  from bs4 import BeautifulSoup
  import pandas as pd
  ```
  
2. Using R visulization of downloaded results:
  
   Packages used in R script:
   ```{r}
    library(wordcloud2)
    library(dplyr)
    library(ggplot2)
    library(lubridate)
    library(stringr)
    library(data.table)
    ```


3. Some plots of results

The trend of number of submitted papers

![](https://github.com/Yiguan/crawl_bioRxiv/blob/master/bioRxiv1.png)

Wordcloud of all papers titles
![](https://github.com/Yiguan/crawl_bioRxiv/blob/master/bioRxiv2.png)


4. Data 

By Jun 7, 2019

<https://github.com/Yiguan/crawl_bioRxiv/blob/master/biorxiv.csv>
