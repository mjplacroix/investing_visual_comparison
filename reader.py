# remeber to start/load pip environment
# > pipenv shell

# define an empty list
tickers = []

# open file and read the content in a list
with open('stock_list_5.txt', 'r') as stock_list:
    for line in stock_list:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        tickers.append(currentPlace)

import csv
from datetime import date
from iexfinance.stocks import Stock, get_historical_data, iexcloud-messages-used

today = date.today()
d3 = today.strftime("%m_%d_%y")

# get lastest price day of
with open(f'm{d3}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ticker", f"{d3}"])
    for symbol in tickers:
        a = Stock(f"{symbol}")
        info = a.get_quote()
        price = info["latestPrice"]
        print(symbol, price, iexcloud-messages-used)
        writer.writerow([symbol, f"{price}"])


# # Iterate over key/value pairs in dict and print them
# for key, value in student_score.items():
#     print(key, ' : ', value)