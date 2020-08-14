from datetime import timedelta, date
from iexfinance.stocks import Stock, get_historical_data
import requests


url = 'https://sandbox.iexapis.com/v1/stock/aapl/chart/date/20180418?chartByDay=True&token=Tpk_13aecb7621784b19bbd53a1c96eeaa3d'
                                    /stock/{symbol}/chart/{range}/{date}
response = requests.get(url)
print(response.headers['iexcloud-messages-used'])
print(response.text)
# for header in response.headers:
#     print(header)


"""
end_date = date.fromisoformat('2020-07-31')
tickers = ['TSLA', 'NFLX', 'GOOGL', 'BRK.B']

# get lastest price day of
for symbol in tickers:
    for i in range(0, 5):
        delta = timedelta(weeks=i)
        date_request = end_date-delta
        info = get_historical_data(symbol, date_request, date_request, output_format='pandas')

        # info = a.get_historical_prices(close_only=date_request)

        print(symbol, date_request, info)
"""