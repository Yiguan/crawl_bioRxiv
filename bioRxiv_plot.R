devtools::install_github("lchiffon/wordcloud2")
library(wordcloud2)
library(dplyr)
library(ggplot2)
library(lubridate)

my_df <- read.csv("biorxiv.csv")

# summary date
my_date <- data.frame(table(my_df$date))
my_date$Var1 <- as.Date(my_date$Var1, "%Y_%m_%d")

# by month
my_date %>% group_by(month = floor_date(Var1, "month")) %>% 
  summarise(num=sum(Freq)) %>% .[1:nrow(.)-1,] -> month_df

my_date$By <- "Per_day"
names(my_date) <- c("Time", "Num_Papers","By")
month_df$By <- "Per_month"
names(month_df) <- c("Time", "Num_Papers","By")
plot_df <- rbind(my_date,month_df)
# plot data
ggplot(plot_df, aes(x=Time,y=Num_Papers)) + theme_bw() + geom_line() + 
  facet_grid(rows = vars(By), scales = "free_y") + scale_x_date(name = "Date", date_breaks = "1 year", date_labels =  "%Y-%m") +
  ylab("Number of submitted papers on bioRxiv")



# world cloud
library(stringr)
library(data.table)

all_title <- paste(my_df$title, collapse = " ")
# clean data
all_title %>% str_replace_all(.,",","") %>% str_replace_all(.,":","") %>%
  str_replace_all(.,"\\.","") %>% str_replace_all(.,"\\?","") %>% tolower(.) %>% 
  str_replace_all(.,"cells","cell") %>% str_replace_all(.,"dynamics","dynamic") %>%
  str_replace_all(.,"genes","gene") %>% str_replace_all(.,"effects","effect") %>%
  str_replace_all(.,"functions","function") %>% str_replace_all(.,"networks","network") %>%
  str_replace_all(.,"neurons","neuron") %>% str_replace_all(.,"sequences","sequence") %>%
  str_replace_all(.,"proteins","protein") %>% str_replace_all(.,"factors","factor") %>% 
  str_replace_all(.,"models","model")-> all_title_clean
words <- strsplit(all_title_clean," ")
words_freq <- data.table(table(unlist(words)))
# select word starts with letters
remove_words <- c("of","a","for","in","and","the","from","with","to","by","an","at","as","is","are",
                  "not","during","into","its","after","between","on")
words_freq[V1 %like% "^[a-z]",][!(V1 %in% remove_words),] -> plot_data
wordcloud2(plot_data, size = 1)
