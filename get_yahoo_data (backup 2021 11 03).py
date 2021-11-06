


# !!! python pass vs continue!!!
# pass is simply a placeholder (it does nothing but passes execution to the next statement)
# continue tells the loop to continue as if it had just restarted
# continue skips the loop's current iteration and executes the next iteration.

# import keyword
# keyword.kwlist

# reticulate::repl_python()

# Upgrade module in terminal:
# pip install yfinance --upgrade 

# Import modules
import yahoo_fin.stock_info as si
import pandas as pd
# from datetime import date
from datetime import datetime
import time
# import feather

# quote = si.get_quote_table("aapl")
# quote["PE Ratio (TTM)"] # 22.71


# val = si.get_stats_valuation("aapl")
# val = val.iloc[1:2, :2]
 
# val.columns = ["Attribute", "Recent"]

# trailing_pe = val.Attribute.str.contains("Trailing P/E")
# float(val[trailing_pe].iloc[0, 1])
# float(val[val.Attribute.str.contains("Price/Sales")].iloc[0,1])


##### dow_list = si.tickers_dow() # Not used
# sp500_list = si.tickers_sp500()
# nasdaq_list = si.tickers_nasdaq()
# type(nasdaq_list)
# len(nasdaq_list)

# tickers_sp500_nasdaq = sorted(sp500_list + nasdaq_list)
today = datetime.now().strftime("(%Y %m %d)")
# tickers_df = pd.DataFrame(tickers_sp500_nasdaq, columns = ["ticker"])
# tickers_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/tickers_sp500_nasdaq.csv", index = False)

tickers_sp500_nasdaq = pd.read_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/tickers_sp500_nasdaq.csv")
tickers_sp500_nasdaq = sorted(tickers_sp500_nasdaq.values.flatten().tolist())
all_tickers = tickers_sp500_nasdaq
# 'PLTR' in all_tickers


tickers_with_clean_prices = pd.read_table("C:/Users/user/Desktop/Aaron/R/Projects/Fundamentals-Data-data/cleaned data/tickers_with_clean_prices.txt").values.flatten()
all_tickers = tickers_with_clean_prices.tolist()
# len(all_tickers)
# 'PLTR' in all_tickers


# Get sector data
import yfinance as yf
# import html5lib

def get_profile_data(tickers):

    # tickers = all_tickers
    # n_tickers = len(all_tickers)
    # i = 1
    # print(str(i) + " of " + str(n_tickers))

    today = datetime.today().strftime("%Y_%m_%d")
    df = pd.DataFrame() # columns = fields)
    
    fields_to_remove = [#'impliedSharesOutstanding', 
    'threeYearAverageReturn', 'volume24Hr', 'bookValue', 
    'revenueQuarterlyGrowth', '52WeekChange', 
    'annualHoldingsTurnover', 'isEsgPopulated', 
    'exchangeTimezoneName', 'dayHigh', 'fiftyTwoWeekLow', 
    'fromCurrency', 'dayLow', 'marketCap', 'startDate', 
    'expireDate', 'previousClose', 'maxAge', 
    'regularMarketOpen', 'lastCapGain', 'category', 
    'fiveYearAverageReturn', 'regularMarketPrice', 
    'priceToBook', 'dateShortInterest', 'SandP52WeekChange',
    'algorithm', 'annualReportExpenseRatio', 'ask', 
    'askSize', 'averageVolume10days', 'beta', 'beta3Year',
    'bid', 'bidSize', 'circulatingSupply', 'companyOfficers',
    'dividendRate', 'dividendYield', 'earningsQuarterlyGrowth',
    'exDividendDate', 'exchangeTimezoneShortName', 
    'fiftyDayAverage', 'fiftyTwoWeekHigh', 'fundFamily',
    'fundInceptionDate', 'gmtOffSetMilliseconds',
    'lastDividendDate', 'lastMarket', 'legalType',
    'maxSupply', 'messageBoardId', 'morningStarOverallRating',
    'morningStarRiskRating', 'navPrice', 'open',
    'openInterest', 'phone', 'priceHint', 'profitMargins',
    'regularMarketDayHigh', 'regularMarketDayLow',
    'regularMarketPreviousClose', 'regularMarketVolume',
    'sharesPercentSharesOut', 'sharesShortPreviousMonthDate',
    'state', 'strikePrice', 'toCurrency', # 'totalAssets',
    'tradeable', 'twoHundredDayAverage', 'volume',
    'volumeAllCurrencies', 'yield', 'ytdReturn', 'zip',
    'address1', 'averageVolume', 'city', 'logo_url',
    'mostRecentQuarter', 'netIncomeToCommon', 'nextFiscalYearEnd',
    'priceToSalesTrailing12Months', 'quoteType',
    # 'sharesShort', 'sharesShortPriorMonth', 
    # 'shortPercentOfFloat', 
    'trailingAnnualDividendRate',
    'trailingAnnualDividendYield', 'trailingEps',
    # 'website', 
    'trailingPE', 'uuid', 'underlyingSymbol',
    'underlyingExchangeSymbol', 'headSymbol', 
    'address2', 'fax']
    # tickers = ['AACQW', 'AAPL'] #, 'SBUX', 'AACQW']
    for ticker in tickers:
        
        if ticker == tickers[1] or ticker == tickers[len(tickers) -1]:
            print(ticker)
            
        # ticker = 'A' #'JMPNL'
        
        ticker_data = yf.Ticker(ticker)
        try:
            profile_i = ticker_data.info
        except (ImportError, IndexError) as e:
            print(" - Error occurred:", e)
            continue
            # pass
        for f in fields_to_remove:
            if f in profile_i.keys():
                del profile_i[f]
        
        profile_i.update({'ticker': ticker})
        profile_i.update({'date': today})
        df = df.append(profile_i, ignore_index = True)
    return(df)



step = 100
start = list(range(0, len(all_tickers), step))
end = [x + step for x in start]
end[len(end)-1] = len(all_tickers)

today = datetime.now().strftime("(%Y %m %d)")


# Get and save 
for i in range(0, len(start)):
  # i = 0
  start_i = start[i]
  end_i = end[i]
  profile_data = get_profile_data(tickers = all_tickers[start_i:end_i])
  profile_data.to_csv(print('C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data %d-%d %s.csv' % (start_i, end_i, today)), index = False)



# len(nasdaq_unique)
# tickers = "AACQ" # problem
# len(all_tickers)
# profile_data_1 = get_profile_data(tickers = all_tickers[0:300])
# profile_data_1.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[0] + "_" + all_tickers[300] + " " + today + ".csv", index = False)
# 
# profile_data_2 = get_profile_data(tickers = all_tickers[301:600])
# profile_data_2.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[301] + "_" + all_tickers[600] + " " + today + ".csv", index = False)
# 
# profile_data_3 = get_profile_data(tickers = all_tickers[601:900])
# profile_data_3.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[601] + "_" + all_tickers[900] + " " + today + ".csv", index = False)
# 
# profile_data_4 = get_profile_data(tickers = all_tickers[901:1200])
# profile_data_4.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[901] + "_" + all_tickers[1200] + " " + today + ".csv", index = False)
# 
# profile_data_5 = get_profile_data(tickers = all_tickers[1201:1500])
# profile_data_5.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[1201] + "_" + all_tickers[1500] + " " + today + ".csv", index = False)
# 
# profile_data_6 = get_profile_data(tickers = all_tickers[1501:1800])
# profile_data_6.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[1501] + "_" + all_tickers[1800] + " " + today + ".csv", index = False)
# 
# profile_data_7 = get_profile_data(tickers = all_tickers[1801:2100])
# profile_data_7.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[1801] + "_" + all_tickers[2100] + " " + today + ".csv", index = False)
# 
# profile_data_8 = get_profile_data(tickers = all_tickers[2101:2400])
# profile_data_8.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[2101] + "_" + all_tickers[2400] + " " + today + ".csv", index = False)
# 
# profile_data_9 = get_profile_data(tickers = all_tickers[2401:2700])
# profile_data_9.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[2401] + "_" + all_tickers[2700] + " " + today + ".csv", index = False)
# 
# 
# profile_data_10 = get_profile_data(tickers = all_tickers[2701:(len(all_tickers)-1)])
# profile_data_10.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data " + all_tickers[2701] + "_" + all_tickers[(len(all_tickers)-1)] + " " + today + ".csv", index = False)
# 
# del profile_data # clear from memory?
# ~5mins


# Get data in the current column for each stock's valuation table
# sp500_stats = {}
# for ticker in sp500_list:
#     temp = si.get_stats_valuation(ticker)
#     temp = temp.iloc[:,:2]
#     temp.columns = ["Attribute", "Recent"]
#  
#     sp500_stats[ticker] = temp
 
 
# combine all the stats valuation tables into a single data frame
# combined_stats = pd.concat(sp500_stats)
# combined_stats = combined_stats.reset_index()

# Remove a column 
# del combined_stats["level_1"]
 
# update column names
# combined_stats.columns = ["ticker", "field", "value"]


# today = date.today()
# combined_stats['date'] = today

# type(combined_stats)
# combined_stats.to_csv("combined_stat " + today + ".csv")
# type(combined_stats)

# combined_stats.to_feather("sp500_combined_stats " + today + ".ftr")
# sp500_stats = pd.read_feather("sp500_combined_stats.ftr")


# combined_stats[combined_stats.Attribute.str.contains("Trailing P/E") # "Price/Sales", "Price/Book", "PEG", "Forward P/E"


#------------------------------------------------#



# sp500_extra_stats = {}
# for ticker in sp500_list:
#     sp500_extra_stats[ticker] = si.get_stats(ticker)
#      
#  
# combined_extra_stats = pd.concat(sp500_extra_stats)
#  
# combined_extra_stats = combined_extra_stats.reset_index()
#  
# del combined_extra_stats["level_1"]
#  
# combined_extra_stats.columns = ["ticker", "field", "value"]



# combined_extra_stats['date'] = today

# type(combined_stats)
# combined_extra_stats.to_csv("combined_extra_stats " + today + ".csv")
# type(combined_stats)

# have to do some grep replacement of B/M to x1000000000, ...
# combined_extra_stats.to_feather("sp500_combined_extra_stats " + today + ".ftr")








# combined_extra_stats[combined_extra_stats.field.str.contains("Return on Equity")] # "Return on Assets", "Profit Margin"


def get_fundamentals_data(tickers):

    # Get balance sheets
    # sheet = si.get_balance_sheet("aapl")
    
    # sheet.loc["cash"] # "totalStockholderEquity", "totalAssets"
    
    # Get balance sheets for many stocks at once
    balance_sheets = {}
    for ticker in tickers:
        try:
            balance_sheets[ticker] = si.get_balance_sheet(ticker)
        except:
            continue
        
    
    # type(balance_sheets)
    # pd.DataFrame.from_dict(balance_sheets, orient ='index') 
    
    bs_df = pd.concat(balance_sheets)
    bs_df = bs_df.reset_index()
    
    today = datetime.now().strftime("(%Y %m %d)")
    
    
    
    bs_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    # bs_df.columnsto_feather("balance_sheets.ftr")
    # type(bs_df)
    
    
    # recent_sheets = {ticker : sheet.iloc[:,:1] for ticker,sheet in balance_sheets.items()}
     
    # for ticker in recent_sheets.keys():
    #     recent_sheets[ticker].columns = ["Recent"]
     
     
    # combine all balance sheets together
    # combined_sheets = pd.concat(recent_sheets)
     
    # reset index to pull in ticker
    # combined_sheets = combined_sheets.reset_index()
     
    # update column names
    # combined_sheets.columns = ["Ticker", "Breakdown", "Recent"]
    
    
    # combined_sheets[combined_sheets.Breakdown == "totalAssets"]
    
    
    
    #-------------------------------------------------------#
    
    
    
    
    
    # income = si.get_income_statement("aapl")
    
    # income.loc["totalRevenue"]
    # income.loc["grossProfit"]
    
    # Get the income statement for multiple stocks
    income_statements = {} # initialize a dict
    for ticker in tickers:
        try:
            income_statements[ticker] = si.get_income_statement(ticker)
        except:
            continue
    
    ist = pd.concat(income_statements)
    ist = ist.reset_index()
    ist.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    # recent_income_statements = {ticker : sheet.iloc[:,:1] for ticker,sheet in income_statements.items()}
     
    # for ticker in recent_income_statements.keys():
    #     recent_income_statements[ticker].columns = ["Recent"]
    #  
    # combined_income = pd.concat(recent_income_statements)
    # combined_income = combined_income.reset_index()
    # combined_income.columns = ["Ticker", "Breakdown", "Recent"]
    # combined_income[combined_income.Breakdown == "totalRevenue"]
    
    
    # flow = si.get_cash_flow("aapl")
    
    
    # Get the cash flow statements of multiple stocks
    cash_flows = {}
    for ticker in tickers:
        try:
            cash_flows[ticker] = si.get_cash_flow(ticker)
        except:
            continue
    
    
    cf = pd.concat(cash_flows)
    cf = cf.reset_index()
    cf.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flows " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv")

    # recent_cash_flows = {ticker : flow.iloc[:,:1] for ticker,flow in cash_flows.items()}
     
     
     
    # for ticker in recent_cash_flows.keys():
    #     recent_cash_flows[ticker].columns = ["Recent"]
     
    # combined_cash_flows = pd.concat(recent_cash_flows)
    # combined_cash_flows = combined_cash_flows.reset_index()
    # combined_cash_flows.columns = ["Ticker", "Breakdown", "Recent"]



# dfn = pd.DataFrame({'A': ['200B', '234M'],
#                     'B': ['123M', '567K']})
# 
# dfn.replace(regex=r'B$', value='000000000')






# Import modules
import pandas as pd
from datetime import date
import yfinance as yf
import yahoo_fin.stock_info as si
  
# Get financial statement data (bs, cf, is, yearly & quarterly)
def get_data(tickers):
    #-------#
    # tickers = ['A', 'AAPL', 'MSFT']
    # i = tickers[1]
    # period = "quarterly"
    #-------#

    # Initialize dataframes
    df_master = dict()
    df_income_statement_yearly = pd.DataFrame()
    df_income_statement_quarterly = pd.DataFrame()
    df_cash_flow_yearly = pd.DataFrame()
    df_cash_flow_quarterly = pd.DataFrame()
    df_balance_sheet_yearly = pd.DataFrame()
    df_balance_sheet_quarterly = pd.DataFrame()
    
    # Current date
    today = datetime.now().strftime("(%Y %m %d)")    
    
    for i in tickers:
        # i = 'SJI'
        # i = all_tickers[3]
        if i == tickers[0]:
            print("start: " + i)
            
        if i == tickers[len(tickers) - 1]:
            print("end: " + i)

        #~~~~~~~~~~~~~~~~#
        # Get all data
        #~~~~~~~~~~~~~~~~#
        
        # time.sleep(5)
        
        try:
            ticker_data = yf.Ticker(i)        
        except (HTTPError, ValueError, KeyError, ImportError, IndexError) as e:
            # If the ticker data cannot be downloaded, skip to next ticker
            continue
            print(" - Error occurred:", e)
    
        if len(ticker_data.financials) == 0:
          continue
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Annual cash flow statements
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        try:
            cash_flow_statement_a = ticker_data.cashflow # yearly
            # Make the index a column
            cash_flow_statement_a = cash_flow_statement_a.reset_index()
            cash_flow_statement_a['ticker'] = i
            try:
                cash_flow_statement_a = pd.melt(cash_flow_statement_a, id_vars=['ticker', 'index'], var_name = 'date')    
            except (ValueError, KeyError, ImportError, IndexError) as e:
                # print(" - Error occurred:", e)
                continue  
            cash_flow_statement_a.columns = ['ticker', 'field', 'report_date', 'value']
            df_cash_flow_yearly = df_cash_flow_yearly.append(cash_flow_statement_a, ignore_index = True)
        except (ValueError, KeyError, ImportError, IndexError) as e:
            # If the data cannot be selected, proceed below
            continue
            # print(" - Error occurred:", e)
            
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Quarterly cash flow statements
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        try:
            cash_flow_statement_q = ticker_data.quarterly_cashflow
            # Make the index a column
            cash_flow_statement_q = cash_flow_statement_q.reset_index()
            cash_flow_statement_q['ticker'] = i
            try:
                cash_flow_statement_q = pd.melt(cash_flow_statement_q, id_vars=['ticker', 'index'], var_name = 'date')    
            except (ValueError, KeyError, ImportError, IndexError) as e:
                # print(" - Error occurred:", e)
                continue  
            cash_flow_statement_q.columns = ['ticker', 'field', 'report_date', 'value']
            df_cash_flow_quarterly = df_cash_flow_quarterly.append(cash_flow_statement_q, ignore_index = True)
        except (ValueError, KeyError, ImportError, IndexError) as e:
            # If the data cannot be selected, proceed below
            continue
            # print(" - Error occurred:", e)
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Yearly income statements
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        try:
            income_statement_a = ticker_data.financials
            # Make the index a column
            income_statement_a = income_statement_a.reset_index()
            income_statement_a['ticker'] = i
            try:
                income_statement_a = pd.melt(income_statement_a, id_vars=['ticker', 'index'], var_name = 'date')    
            except (ValueError, KeyError, ImportError, IndexError) as e:
                # print(" - Error occurred:", e)
                continue  
            income_statement_a.columns = ['ticker', 'field', 'report_date', 'value']
            df_income_statement_yearly = df_income_statement_yearly.append(income_statement_a, ignore_index = True)
        except (ValueError, KeyError, ImportError, IndexError) as e:
            # If the data cannot be selected, proceed below
            continue
            # print(" - Error occurred:", e)
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Quarterly income statements
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        try:
            income_statement_q = ticker_data.quarterly_financials
            # Make the index a column
            income_statement_q = income_statement_q.reset_index()
            income_statement_q['ticker'] = i
            try:
                income_statement_q = pd.melt(income_statement_q, id_vars=['ticker', 'index'], var_name = 'date')    
            except (ValueError, KeyError, ImportError, IndexError) as e:
                # print(" - Error occurred:", e)
                continue  
            income_statement_q.columns = ['ticker', 'field', 'report_date', 'value']
            df_income_statement_quarterly = df_income_statement_quarterly.append(income_statement_q, ignore_index = True)
        except (ValueError, KeyError, ImportError, IndexError) as e:
            # If the data cannot be selected, proceed below
            continue
            # print(" - Error occurred:", e)
    
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Yearly balance sheets
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        try:
            balance_sheet_a = ticker_data.balance_sheet
            # Make the index a column
            balance_sheet_a = balance_sheet_a.reset_index()
            balance_sheet_a['ticker'] = i
            try:
                balance_sheet_a = pd.melt(balance_sheet_a, id_vars=['ticker', 'index'], var_name = 'date')    
            except (ValueError, KeyError, ImportError, IndexError) as e:
                # print(" - Error occurred:", e)
                continue  
            balance_sheet_a.columns = ['ticker', 'field', 'report_date', 'value']
            df_balance_sheet_yearly = df_balance_sheet_yearly.append(balance_sheet_a, ignore_index = True)
        except (ValueError, KeyError, ImportError, IndexError) as e:
            # If the data cannot be selected, proceed below
            continue
            # print(" - Error occurred:", e)
    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Quarterly balance sheets
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        try:
            balance_sheet_q = ticker_data.quarterly_balance_sheet
            # Make the index a column
            balance_sheet_q = balance_sheet_q.reset_index()
            balance_sheet_q['ticker'] = i
            try:
                balance_sheet_q = pd.melt(balance_sheet_q, id_vars=['ticker', 'index'], var_name = 'date')    
            except (ValueError, KeyError, ImportError, IndexError) as e:
                # print(" - Error occurred:", e)
                continue  
            balance_sheet_q.columns = ['ticker', 'field', 'report_date', 'value']
            df_balance_sheet_quarterly = df_balance_sheet_quarterly.append(balance_sheet_q, ignore_index = True)
        except (ValueError, KeyError, ImportError, IndexError) as e:
            # If the data cannot be selected, proceed below
            continue
            # print(" - Error occurred:", e)
    
    # Collect all objects into the dict
    df_master['cash_flow_yearly'] = df_cash_flow_yearly
    df_master['cash_flow_quarterly'] = df_cash_flow_quarterly
    df_master['income_statement_yearly'] = df_income_statement_yearly
    df_master['income_statement_quarterly'] = df_income_statement_quarterly
    df_master['balance_sheet_yearly'] = df_balance_sheet_yearly
    df_master['balance_sheet_quarterly'] = df_balance_sheet_quarterly
    
    return df_master


# Current date
# today = date.today().strftime("%Y_%m_%d")
# df = get_data(tickers = ['MSFT', 'AAPL'])
# df['cash_flow_yearly']

# ticker_data = yf.Ticker('MSFT')
# # Forecasts !!!
# ticker_data.calendar
# ticker_data.actions
# ticker_data.history
# ticker_data.institutional_holders



#~~~~~~~~~~~~~~~~~~~~~~~~#
# Download and save data
#~~~~~~~~~~~~~~~~~~~~~~~~#

# tickers = ['CNV', 'MSFT']

# def download_yhoo_data(tickers):
#   
#   # tickers = tickers_sp500_nasdaq
#   
#   i = 1
#   increment = 50
#   
#   ticker_length = len(tickers)
#   
#   while (i-1)*increment < ticker_length:
#   
#     ticker_subset = tickers[((i-1)*increment):(i*increment)]
#     
#     df = get_data(tickers = ticker_subset)
#     
#     bs_a = df['balance_sheet_yearly']
#     bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + ticker_subset[0] + "_" + ticker_subset[len(ticker_subset)-1] + " " + today + ".csv", index = False)
#   
#     bs_q = df['balance_sheet_quarterly']
#     bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + ticker_subset[0] + "_" + ticker_subset[len(ticker_subset)-1] + " " + today + ".csv", index = False)
#     
#     is_a = df['income_statement_yearly']
#     is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + ticker_subset[0] + "_" + ticker_subset[len(ticker_subset)-1] + " " + today + ".csv", index = False)
#     
#     is_q = df['income_statement_quarterly']
#     is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + ticker_subset[0] + "_" + ticker_subset[len(ticker_subset)-1] + " " + today + ".csv", index = False)
#     
#     cf_a = df['cash_flow_yearly']
#     cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + ticker_subset[0] + "_" + ticker_subset[len(ticker_subset)-1] + " " + today + ".csv", index = False)
#     
#     cf_q = df['cash_flow_quarterly']
#     cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + ticker_subset[0] + "_" + ticker_subset[len(ticker_subset)-1] + " " + today + ".csv", index = False)
#   
#     i += 1
#     
#     time.sleep(5)

  
# Slow !!! and Htpp error!!!
# Stops after first batch is downloaded with HTTP error!!
# download_yhoo_data(tickers = tickers_sp500_nasdaq)
  




# all_tickers = all_tickers[0:13] # 13 tickers
# all_tickers[0:5]
# all_tickers[5:10]
# all_tickers[10:14]


step = 50
start = list(range(0, len(all_tickers), step))
end = [x + step for x in start]
end[len(end)-1] = len(all_tickers) + 1

import os
print(os.getcwd())

# Get and save 
# for i in range(0, len(start)):
# parallel processing!!!

# start_i = 0
# end_i = 1



for i in range(0, len(start)):
  start_i = start[i]
  end_i = end[i]
  
  tickers = all_tickers[start_i:end_i]
  df = get_data(tickers = tickers)
  
  bs_a = df['balance_sheet_yearly']
  bs_a.to_csv('./data/balance_sheets_yearly ' + str(start_i) + '-' + str(end_i) + ' ' + str(today) + '.csv', sep=',', index = False)
  
  bs_q = df['balance_sheet_quarterly']
  bs_q.to_csv('./data/balance_sheets_quarterly ' + str(start_i) + '-' + str(end_i) + ' ' + str(today) + '.csv', sep=',', index = False)
  
  is_a = df['income_statement_yearly']
  is_a.to_csv('./data/income_statements_yearly ' + str(start_i) + '-' + str(end_i) + ' ' + str(today) + '.csv', sep=',', index = False)
  
  is_q = df['income_statement_quarterly']
  is_q.to_csv('./data/income_statements_quarterly ' + str(start_i) + '-' + str(end_i) + ' ' + str(today) + '.csv', sep=',', index = False)
  
  cf_a = df['cash_flow_yearly']
  cf_a.to_csv('./data/cash_flow_statements_yearly ' + str(start_i) + '-' + str(end_i) + ' ' + str(today) + '.csv', sep=',', index = False)
  
  cf_q = df['cash_flow_quarterly']
  cf_q.to_csv('./data/cash_flow_statements_quarterly ' + str(start_i) + '-' + str(end_i) + ' ' + str(today) + '.csv', sep=',', index = False)
  
  perc = (i+1) / (len(start)+1)*100 
  print("%d%% done!" % perc)
  
  
  
# some printed at intervals of 10 mins


#6:05 start
  
# df.keys()
  
# time.sleep(5)

# tickers.append('AES')
# tickers = all_tickers[0:5]
# tickers = all_tickers[0:200]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# tickers = all_tickers[201:400]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# 
# tickers = all_tickers[401:600]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# tickers = all_tickers[601:800]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# tickers = all_tickers[801:1000]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# time.sleep(5)
# 
# tickers = all_tickers[1001:1200]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# tickers = all_tickers[1201:1400]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# time.sleep(5)
# 
# tickers = all_tickers[1401:1600]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# tickers = all_tickers[1601:1800]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# tickers = all_tickers[1801:2000]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# tickers = all_tickers[2001:2200]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# time.sleep(5)
# 
# tickers = all_tickers[2201:2400]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# tickers = all_tickers[2401:2600]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# tickers = all_tickers[2601:2800]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# time.sleep(5)
# 
# tickers = all_tickers[2801:3000]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# tickers = all_tickers[3001:3200]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# 
# 
# time.sleep(5)
# 
# tickers = all_tickers[3201:3400]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# tickers = all_tickers[3401:3600]
# 
# # HTTPError: HTTP Error 503: Service Unavailable
# # last ticker RELIW (this or next ticker http error?)
# 
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# time.sleep(5)
# 
# tickers = all_tickers[3601:3800]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# 
# time.sleep(5)
# 
# tickers = all_tickers[3801:4000]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# time.sleep(5)
# 
# tickers = all_tickers[4001:4200]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# time.sleep(5)
# 
# tickers = all_tickers[4201:4400]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# time.sleep(5)
# 
# tickers = all_tickers[4401:4600]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# time.sleep(5)
# 
# tickers = all_tickers[4601:4800]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# time.sleep(5)
# 
# tickers = all_tickers[4801:5000]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# time.sleep(5) 
# 
# tickers = all_tickers[5001:5200]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q
# 
# time.sleep(5) 
# 
# 
# tickers = all_tickers[5201:5400]
# df = get_data(tickers = tickers)
# bs_a = df['balance_sheet_yearly']
# bs_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# bs_q = df['balance_sheet_quarterly']
# bs_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_a = df['income_statement_yearly']
# is_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# is_q = df['income_statement_quarterly']
# is_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_a = df['cash_flow_yearly']
# cf_a.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# cf_q = df['cash_flow_quarterly']
# cf_q.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flow_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
# 
# 
# # Clear some memory resources?
# del tickers
# del df
# del bs_a
# del bs_q
# del is_a
# del is_q
# del cf_a
# del cf_q


# pd.set_option('display.max_columns', 11)
# ticker_data.history(period = "max")


        # ticker_data.history(period = "max")
        
        # ticker_data.actions
        # ticker_data.dividends
        # ticker_data.splits
        # ticker_data.major_holders
        # ticker_data.calendar

