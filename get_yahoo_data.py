
################
# RULES
# Need to run code selections by selecting full row, otherwise might not run
# If there are dots ('...') in the console, then it is necessary to push 'Enter' in console.
# If there is a empty line ('   ') in the console, then it is running.
################

# !!! python pass vs continue!!!
# pass is simply a placeholder (it does nothing but passes execution to the next statement)
# continue tells the loop to continue as if it had just restarted
# continue skips the loop's current iteration and executes the next iteration.


# Upgrade module in terminal:
# pip install yfinance --upgrade 

# Import modules ---
import yahoo_fin.stock_info as si # for fundamentals, etc.
import pandas as pd
# from datetime import date
from datetime import datetime
import time
import yfinance as yf # Used to get profile data, but maybe can use si instead
# import feather

today = datetime.now().strftime("(%Y %m %d)")



# quote = si.get_quote_table("aapl")
# quote["PE Ratio (TTM)"] # 22.71

# val = si.get_stats_valuation("aapl")
# val = val.iloc[1:2, :2]
# val.columns = ["Attribute", "Recent"]

# trailing_pe = val.Attribute.str.contains("Trailing P/E")
# float(val[trailing_pe].iloc[0, 1])
# float(val[val.Attribute.str.contains("Price/Sales")].iloc[0,1])


## dow_list = si.tickers_dow() # Not used
# sp500_list = si.tickers_sp500()
# nasdaq_list = si.tickers_nasdaq()
# type(nasdaq_list)
# len(nasdaq_list)

# tickers_sp500_nasdaq = sorted(sp500_list + nasdaq_list) # Get unique set

# tickers_df = pd.DataFrame(tickers_sp500_nasdaq, columns = ["ticker"])
# tickers_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/tickers_sp500_nasdaq.csv", index = False)

tickers_sp500_nasdaq = pd.read_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/tickers_sp500_nasdaq.csv")
tickers_sp500_nasdaq = sorted(tickers_sp500_nasdaq.values.flatten().tolist())
all_tickers = tickers_sp500_nasdaq
# len(all_tickers) # 5,224 tickers
# 'PLTR' in tickers_sp500_nasdaq

tickers_with_clean_prices = pd.read_table("C:/Users/user/Desktop/Aaron/R/Projects/Fundamentals-Data-data/cleaned data/tickers_with_clean_prices.txt").values.flatten()
all_tickers = tickers_with_clean_prices.tolist()
# len(all_tickers) # 13,762

# Find tickers in S&P500 or NASDAQ that also have clean downloaded prices
s_all_tickers = set(all_tickers)
s_tickers_sp500_nasdaq = set(tickers_sp500_nasdaq)
all_tickers = s_all_tickers.intersection(s_tickers_sp500_nasdaq) # set
all_tickers = list(all_tickers) # convert set to list
len(all_tickers)

all_tickers.append('PLTR')
all_tickers.append('SOFI')
all_tickers = sorted(all_tickers)
# 'PLTR' in all_tickers


# Get sector data
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



# tickers = "AACQ" # problem

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



# sp500_extra_stats = {}
# for ticker in sp500_list:
#     sp500_extra_stats[ticker] = si.get_stats(ticker)


# have to do some grep replacement of B/M to x1000000000, ...
# combined_extra_stats.to_feather("sp500_combined_extra_stats " + today + ".ftr")


# sheet = si.get_balance_sheet('MSFT')
# sheet = si.get_quote_data('AAPL')

# combined_extra_stats[combined_extra_stats.field.str.contains("Return on Equity")] # "Return on Assets", "Profit Margin"


# Company officers
company_officers = si.get_company_officers('AAPL')
company_officers = pd.DataFrame(company_officers) # Name, totalpay, ...
company_officers.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/company_officers.csv", index = False)

# analyst_info = si.get_analysts_info('AAPL')
# analyst_info = pd.DataFrame(analyst_info)
# pd.DataFrame.from_dict(analyst_info, orient = 'index')

# Basic profile data
profile_data = si.get_company_info('AAPL')
profile_data = pd.DataFrame(profile_data) 
profile_data.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/profile_data.csv", index = False)

earnings_history = si.get_earnings_history('AAPL') # EPS surprise, etc. across many years
earnings_history = pd.DataFrame(earnings_history)
earnings_history.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/earnings_history.csv", index = False)

# si.get_data('AAPL') # Price data

# Balance sheets, income statements, cash flow statements
financials = si.get_financials('AAPL') 


# Function to get and save balance sheets, income statements, and
#  cash flow statements from Yahoo
def get_fundamentals_data(tickers):

    # sheet = si.get_balance_sheet("aapl")
    # sheet.loc["cash"] # "totalStockholderEquity", "totalAssets"
    
    #################
    # tickers = all_tickers[0:3]
    # tickers.append('VIMBEO') # Add fictitious ticker
    # tickers = ['ADAP', 'ADBE']
    #################
  
    yearly_income_statements = {} # create dict  
    quarterly_income_statements = {} # create dict  
    yearly_balance_sheets = {} # create dict
    quarterly_balance_sheets = {} # create dict
    yearly_cash_flows = {} # Create dict
    quarterly_cash_flows = {} # Create dict
    # tickers_errors = []
    i = 0
  
    # tickers = all_tickers[0:100]
    for ticker in tickers:
    
      ######
      # ticker = 'ADBE'
      ######
      
      # print(ticker)
      
      try:
        # Get financial statements
        fin_data_i = si.get_financials(ticker)  
        # fin_data_i.keys()
        
        if len(fin_data_i) == 0:
            # tickers_errors.append(ticker + ' - length of zero')
            continue
        
        # Yearly income statements
        is_y = fin_data_i['yearly_income_statement']
        
        # Move axis data to column
        is_y = is_y.reset_index()
        # Add ticker name
        is_y.insert(loc=0, column = 'ticker', value = str(ticker))
        
        is_y = is_y.melt(id_vars = ['ticker', 'Breakdown'])
        
        is_y.columns = ['ticker', 'field', 'date', 'value']
        
        yearly_income_statements[i] = is_y
        
        # Quarterly income statements
        is_q = fin_data_i['quarterly_income_statement']
        # Move axis data to column
        is_q = is_q.reset_index()
        # Add ticker name
        is_q.insert(loc=0, column = 'ticker', value = str(ticker))
        
        is_q = is_q.melt(id_vars = ['ticker', 'Breakdown'])
        
        is_q.columns = ['ticker', 'field', 'date', 'value']
        
        quarterly_income_statements[i] = is_q
        
        # Yearly balance sheets
        bs_y = fin_data_i['yearly_balance_sheet']
        # Move axis data to column
        bs_y = bs_y.reset_index()
        # Add ticker name
        bs_y.insert(loc=0, column = 'ticker', value = str(ticker))
        
        bs_y = bs_y.melt(id_vars = ['ticker', 'Breakdown'])
        
        bs_y.columns = ['ticker', 'field', 'date', 'value']
        
        yearly_balance_sheets[i] = bs_y
        
        
        # Quarterly balance sheets
        bs_q = fin_data_i['quarterly_balance_sheet']
        # Move axis data to column
        bs_q = bs_q.reset_index()
        # Add ticker name
        bs_q.insert(loc=0, column = 'ticker', value = str(ticker))
        
        bs_q = bs_q.melt(id_vars = ['ticker', 'Breakdown'])
        
        bs_q.columns = ['ticker', 'field', 'date', 'value']
        
        quarterly_balance_sheets[i] = bs_q
        
        
        # Yearly cash flows
        cf_y = fin_data_i['yearly_cash_flow']
        # Move axis data to column
        cf_y = cf_y.reset_index()
        # Add ticker name
        cf_y.insert(loc=0, column = 'ticker', value = str(ticker))
        
        cf_y = cf_y.melt(id_vars = ['ticker', 'Breakdown'])
        
        cf_y.columns = ['ticker', 'field', 'date', 'value']
        
        yearly_cash_flows[i] = cf_y
        
        
        # Quarterly cash flows
        cf_q = fin_data_i['quarterly_cash_flow']
        # Move axis data to column
        cf_q = cf_q.reset_index()
        # Add ticker name
        cf_q.insert(loc=0, column = 'ticker', value = str(ticker))
        
        cf_q = cf_q.melt(id_vars = ['ticker', 'Breakdown'])
        
        cf_q.columns = ['ticker', 'field', 'date', 'value']
        
        quarterly_cash_flows[i] = cf_q
        
      except Exception as e:
        print(ticker, '- error: ', e)
        # tickers_errors.append(str(ticker) + '- error: ' + e))
        continue
          
      # Increase index
      i += 1
  
    today = datetime.now().strftime("(%Y %m %d)")
    
    # Combined all dataframes
    is_y_df = pd.concat(yearly_income_statements)
    is_q_df = pd.concat(quarterly_income_statements)
    bs_y_df = pd.concat(yearly_balance_sheets)
    bs_q_df = pd.concat(quarterly_balance_sheets)
    cf_y_df = pd.concat(yearly_cash_flows)
    cf_q_df = pd.concat(quarterly_cash_flows)
    # tickers_errors_df = pd.DataFrame(tickers_errors)
      
    # Save
    is_y_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    is_q_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/income_statements_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    bs_y_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    bs_q_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/balance_sheets_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    cf_y_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flows_yearly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    cf_q_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/cash_flows_quarterly " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    # tickers_errors_df.to_csv("C:/Users/user/Desktop/Aaron/R/Projects/yahoo data/data/tickers_errors " + tickers[0] + "_" + tickers[len(tickers)-1] + " " + today + ".csv", index = False)
    


# ticker_set = all_tickers[0:3]
# get_fundamentals_data(tickers = ticker_set)


step = 300
start = list(range(0, len(all_tickers), step))
end = [x + step for x in start]
end[len(end)-1] = len(all_tickers) + 1

# import os
# print(os.getcwd())


# parallel processing!!!

for i in range(0, len(start)):

  #######
  # start_i = 0
  # end_i = 1
  #######
  
  start_i = start[i]
  end_i = end[i]

  get_fundamentals_data(tickers = all_tickers[start_i:end_i])




# dfn = pd.DataFrame({'A': ['200B', '234M'],
#                     'B': ['123M', '567K']})
# dfn.replace(regex=r'B$', value='000000000')




# time.sleep(5)
        
# try:
#     ticker_data = yf.Ticker(i)        
# except (HTTPError, ValueError, KeyError, ImportError, IndexError) as e:
            

# parallel processing!!!

# perc = (i+1) / (len(start)+1)*100 
# print("%d%% done!" % perc)
  
  

# tickers.append('AES')
# pd.set_option('display.max_columns', 11)
