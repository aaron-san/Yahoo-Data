
# Clean downloaded YHOO data
#  - The data was downloaded via 'get_yahoo_data.py'


library(tidyverse)
library(data.table)
library(lubridate)

source("C:/Users/user/Desktop/Aaron/R/Projects/Fundamentals-Data/helper functions.R")



# Check that downloaded (csv) content matches file name tickers
# - During download, some tickers had "http error" and broke
#   the download process. 

statement_files <- 
    list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", 
               pattern = "statements|sheets", full.names = TRUE)
first_ticker <- 
    map(statement_files, ~str_extract_all(.x, "[A-Z]+(?=_)")) %>% unlist()
last_ticker <- 
    map(statement_files, ~str_extract_all(.x, "(?<=_)[A-Z]+")) %>% unlist()


statements <- map(statement_files, ~read_tibble(.x))

statement_first_ticker <- statements %>% 
    map_chr(. %>% pull(ticker) %>% unique() %>% .[1]) 

statement_last_ticker <- statements %>% 
    map_chr(. %>% pull(ticker) %>% unique() %>% .[length(.)])

stopifnot(all(statement_first_ticker < statement_last_ticker))





######################################
##### Clean financial statements #####
######################################

today <- str_replace_all(today(), "-", "_")

# Function that: 
# - Removes duplicates, 
# - Reshapes,
#   Drops rows with missing 'req_field's
clean_statement <- function(df) { #, req_field) {
    #------#
    # df <- statements_renamed[[1]]
    # req_field <- "total_assets"
    #------#
    
    df %>% 
        distinct() %>%
        mutate(field = snakecase::to_snake_case(field)) %>%
        drop_na(value) %>% 
        # Select only unique ticker-date-field pairs (ticker QK had some strange duplicate date-field values)
        distinct(ticker, report_date, field, .keep_all = TRUE) %>%
        # pivot_wider(names_from = field, values_from = value) %>%
        # Drop rows with missing 'req_field's
        # drop_na(all_of(req_field)) %>%
        arrange(ticker, report_date) %>%
        distinct()
}



#------------------#
# Balance sheets
#------------------#
bs_yearly_files <- list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", pattern = "balance_sheets_yearly [A-Z]+", full.names = TRUE)
bs_yearly <- 
    map_df(bs_yearly_files,
           ~read_tibble(.x) %>%
               # Rename "date" to "report_date" if "date" exists
               rename(any_of(c("report_date" = "date"))) %>% 
               add_column(period = "yearly")) %>% 
    clean_statement()


bs_quarterly_files <- list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", pattern = "balance_sheets_quarterly [A-Z]+", full.names = TRUE)
bs_quarterly <- map_df(bs_quarterly_files, 
                       ~read_tibble(.x) %>% 
                           # Rename "date" to "report_date" if "date" exists
                           rename(any_of(c("report_date" = "date"))) %>% 
                           add_column(period = "quarterly")) %>% 
    clean_statement()

# Create CSV
fwrite(bs_yearly, paste0("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cleaned/yhoo_balance_sheets_quarterly ", today, ".csv"))
fwrite(bs_quarterly, paste0("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cleaned/yhoo_balance_sheets_yearly ", today, ".csv"))


#---------------------#
# Income statements
#---------------------#
is_yearly_files <- list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", pattern = "income_statements_yearly [A-Z]+", full.names = TRUE)
is_yearly <- map_df(is_yearly_files, 
                    ~read_tibble(.x) %>%
                        # Rename "date" to "report_date" if "date" exists
                        rename(any_of(c("report_date" = "date"))) %>% 
                        add_column(period = "yearly")) %>% 
    clean_statement()


is_quarterly_files <- list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", pattern = "income_statements_quarterly [A-Z]+", full.names = TRUE)
is_quarterly <- map_df(is_quarterly_files, 
                       ~read_tibble(.x) %>% 
                           # Rename "date" to "report_date" if "date" exists
                           rename(any_of(c("report_date" = "date"))) %>% 
                           add_column(period = "quarterly")) %>% 
    clean_statement()


# Create CSV
fwrite(is_yearly, paste0("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cleaned/yhoo_income_statements_yearly ", today, ".csv"))
fwrite(is_quarterly, paste0("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cleaned/yhoo_income_statements_quarterly ", today, ".csv"))


#---------------------#
# Cash flow statements
#---------------------#
cf_yearly_files <- list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", pattern = "cash_flow_statements_yearly [A-Z]+", full.names = TRUE)
cf_yearly <- map_df(cf_yearly_files, 
                    ~read_tibble(.x) %>% 
                        # Rename "date" to "report_date" if "date" exists
                        rename(any_of(c("report_date" = "date"))) %>% 
                        add_column(period = "yearly")) %>% 
    clean_statement()

cf_quarterly_files <- list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", pattern = "cash_flow_statements_quarterly [A-Z]+", full.names = TRUE)
cf_quarterly <- map_df(cf_quarterly_files, 
                       ~read_tibble(.x) %>%
                           # Rename "date" to "report_date" if "date" exists
                           rename(any_of(c("report_date" = "date"))) %>% 
                           add_column(period = "quarterly")) %>% 
    clean_statement()


# Create CSV
fwrite(cf_yearly, paste0("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cleaned/yhoo_cash_flow_statements_yearly ", today, ".csv"))
fwrite(cf_quarterly, paste0("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cleaned/yhoo_cash_flow_statements_quarterly ", today, ".csv"))








######################################
######### Clean profile data #########
######################################


# Merge and clean names of Yahoo data (from "get_yahoo_data.py")
profile_data_raw <- list.files("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data", pattern = "profile_data", full.names = TRUE)

profiles_data <- map_df(profile_data_raw, ~fread(.x)) %>% as_tibble()



profiles <- 
    profiles_data %>% 
    rename(download_date = date) %>% 
    janitor::clean_names() %>% 
    mutate(download_date = as.Date(download_date, "%Y_%m_%d")) %>% 
    select(ticker, download_date, everything()) %>% 
    arrange(ticker, desc(download_date)) %>% 
    # Fill missing sector or industry data
    group_by(ticker) %>% 
    fill(c(sector, industry), .direction = "down") %>% 
    fill(c(sector, industry), .direction = "up") %>% 
    slice(1) %>% 
    ungroup() %>% 
    mutate(industry = snakecase::to_snake_case(industry),
           sector = snakecase::to_snake_case(sector)) %>% 
    select(ticker, download_date, sector, industry, long_business_summary,
           shares_outstanding, short_ratio, 
           held_percent_institutions, peg_ratio) %>% 
    distinct() %>% 
    mutate(across(c(sector, industry), 
                  ~str_to_lower(.x) %>% 
                      # Remove strange characters from strings
                      str_replace_all("[^\u0001-\u007F]", "_") %>% 
                      str_replace_all("\\&", "_and_") %>% 
                      str_replace_all(" ", "_") %>% 
                      str_replace_all("-", "_") %>% 
                      str_replace_all("rei_t", "reit") %>%
                      str_replace_all("_ife", "_life") %>% 
                      str_replace_all("_iversified", "_diversified") %>% 
                      str_replace_all("_ndustrial", "_industrial") %>% 
                      str_replace_all("_ealthcare", "_healthcare") %>% 
                      str_replace_all("_on_alcoholic", "_non_alcoholic") %>% 
                      str_replace_all("_egulated", "_regulated") %>% 
                      str_replace_all("_nfrastructure", "_infrastructure") %>% 
                      str_replace_all("_pplication", "_application") %>% 
                      str_replace_all("_eneral", "_general") %>% 
                      str_replace_all("_ffice", "_office") %>% 
                      str_replace_all("_pecialty", "_specialty") %>% 
                      str_replace_all("_etail", "_retail") %>% 
                      str_replace_all("_esidential", "_residential") %>% 
                      str_replace_all("_egional", "_regional") %>% 
                      str_replace_all("_einsurance", "_reinsurance") %>% 
                      str_replace_all("__", "_") %>% 
                      str_replace_all("__", "_") %>% 
                      str_replace_all("__", "_")))

# profiles %>% distinct(industry)



# Save to this project's data directory
fwrite(profiles, paste0("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cleaned/yhoo_profiles (", gsub("-", " ", today()), ").csv"))



