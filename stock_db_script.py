import sqlite3
import pandas as pd 

# Start by entering your 'pipenv shell' to enable usage of above imports
# connect to the local SQLite DB
cnx = sqlite3.connect('Stocks.db')
c = cnx.cursor()

# read in your most recent CSV
# will need to rename to appropriate date, precended by 'm' for SQL
# can/should prob set the new date/table_name as a variable to insert everywhere
df = pd.read_csv('CSVs/07_04_20.csv')
df.to_sql(name="m07_04_20", con=cnx, index=False)

df = pd.read_csv('CSVs/07_10_20.csv')
df.to_sql(name="m07_10_20", con=cnx, index=False)

df = pd.read_csv('CSVs/07_17_20.csv')
df.to_sql(name="m07_17_20", con=cnx, index=False)
 
current_db_list = c.execute('''SELECT Ticker FROM m07_04_20''')
current_stock_list = []
for line in current_db_list:
    stock = str(line).strip("()'',")
    current_stock_list.append(stock)
print(current_stock_list)

# list of stocks from this week
# change this line to date/name of most recent CSV -> Table
new_stocks = c.execute('''SELECT Ticker FROM m07_10_20''')
new_stock_list = []
for line in new_stocks:
    stock = str(line).strip("()'',")
    new_stock_list.append(stock)
print(new_stock_list)

# find the difference
list_difference = []
for item in new_stock_list:
  if item not in current_stock_list:
    list_difference.append(item)
list_difference = tuple(list_difference)
print(list_difference)


# if len(list_difference) > 0
# select stocks from the new list that are not currently in the database
stmt = f"SELECT Ticker, m07_17_20 FROM m07_17_20 WHERE Ticker NOT IN '{list_difference}'"

# if len(list_different) = 0
# select all the stocks from the new list
stmt = f"SELECT Ticker, m07_17_20 FROM m07_17_20"

stock = c.execute(stmt)

stocks_to_UPDATE = []
for bit in stock:
    stocks_to_UPDATE.append(bit)
stocks_to_UPDATE = tuple(stocks_to_UPDATE)
print(stocks_to_UPDATE)

# add new column with appropriate header (data preceded by 'm')
c.execute('''ALTER TABLE m07_04_20 ADD COLUMN m07_10_20''')

# update the stocks currently in the DB with the new prices
for x, y in stocks_to_UPDATE:
    print(f'X - {x}  Y-{y}')
    stmt = f"UPDATE m07_04_20 SET m07_10_20 = '{y}' WHERE Ticker = '{x}'"
    c.execute(stmt)
    cnx.commit()


# the len(list_difference) was > 0
# query to insert the new stocks
stmt = f"SELECT Ticker, m07_17_20 FROM m07_17_20 WHERE Ticker IN '{list_difference}'"
new_stock_query = c.execute(stmt)

stocks_to_INSERT = []
for bit in new_stock_query:
    stocks_to_INSERT.append(bit)
stocks_to_INSERT = tuple(stocks_to_INSERT)
print(stocks_to_INSERT)


for new in stocks_to_INSERT:
    print(new)
    stmt = f"INSERT INTO m07_04_20(Ticker, m07_22_20) VALUES {new}"
    c.execute(stmt)
    cnx.commit()