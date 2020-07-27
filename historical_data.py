from iexfinance.stocks import get_historical_data
from datetime import datetime

# two lists
# one of the stocks you want to query for
# another of the dates to query for
    # for data
        # query stock prices
        # collect stock prices
        # store each in a weekly CSV
            # or update a single CSV for the year?
# start inputting new weekly data in DB 

tickers = ['TSLA', 'NFLX', 'GOOGL', 'BRK.B', 'SPY', 'IWB']



start = datetime(2020, 7, 1)

for symbol in tickers:
    historical_price = get_historical_data(f"{symbol}", start, close_only=True, token="sk_49ed011aeb6240df92907389567c5159")
    print(f'{symbol} - {historical_price}')

# import csv
# from datetime import date

# today = date.today()
# d3 = today.strftime("%m_%d_%y")

# with open(f'm{d3}.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Ticker", f"{d3}"])
#     for symbol in tickers:
#         a = Stock(f"{symbol}", token="sk_49ed011aeb6240df92907389567c5159")
#         info = a.get_quote()
#         price = info["latestPrice"]
#         print(symbol, price)
#         writer.writerow([symbol, f"{price}"])