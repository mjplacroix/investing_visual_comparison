# remeber to start/load pip environment
# > pipenv shell
import csv
from datetime import date
from iexfinance.stocks import Stock, get_historical_data

today = date.today()
date = today.strftime("%m_%d_%y")


# # define an empty list
tickers = []

# open file and read the content in a list
with open(f'm{date}.csv', 'r') as stock_list:
    for line in stock_list:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        tickers.append(currentPlace)

# import csv
# from datetime import date
# from iexfinance.stoc ks import Stock, get_historical_data

# today = date.today()
# date = today.strftime("%m_%d_%y")

# get lastest price day of
with open(f'm{date}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ticker", f"{date}"])
    for symbol in tickers:
        a = Stock(f"{symbol}")
        info = a.get_quote()
        price = info["latestPrice"]
        print(symbol, price)
        writer.writerow([symbol, f"{price}"])


# # Iterate over key/value pairs in dict and print them
# for key, value in student_score.items():
#     print(key, ' : ', value)