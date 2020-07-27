import sqlite3

""" create new table with starter columns - insert some data """
# conn = sqlite3.connect('Cars.db')  
# c = conn.cursor()
        ### make sure the price column doesn't have a NOT NULL constaint
# c.execute('''CREATE TABLE Cars(Name TEXT, Price INTEGER)''')
# c.execute('''INSERT INTO Cars(Name, Price) VALUES('Audi', 52642)''')
# c.execute('''INSERT INTO Cars(Name, Price) VALUES('Mercedes', 57127)''')
# conn.commit()


""" add additional rows """
# conn = sqlite3.connect('Cars.db')  
# c = conn.cursor()
# c.execute('''INSERT INTO Cars(Name, Price) VALUES('Ford', 29999)''')
# c.execute('''INSERT INTO Cars(Name, Price) VALUES('Tesla', 587127)''')
# conn.commit()

""" add additional columns with ALTER TABLE __ ADD COLUMN """
# conn = sqlite3.connect('Cars.db')  
# c = conn.cursor()
# c.execute('''ALTER TABLE Cars ADD COLUMN Price_3''')
#         ### rename column if mistaken
# # c.execute('''ALTER TABLE Cars RENAME COLUMN current_name TO new_name''')
# c.execute('''INSERT INTO Cars(Name, Price_3) VALUES('Ford', 29999)''')
# c.execute('''INSERT INTO Cars(Name, Price_3) VALUES('Tesla', 299999)''')
# conn.commit()

""" change price """
# conn = sqlite3.connect('Cars.db')
# c = conn.cursor()
# c.execute('''UPDATE Cars SET Price_2 = 232323''')
# conn.commit()

""" Update specific existing row with new column/price """
# # new price column
# conn = sqlite3.connect('Cars.db')  
# c = conn.cursor()
# c.execute('''ALTER TABLE Cars RENAME COLUMN Price_4 TO Price_4''')
# # add ONLY the prices for existing cars
# c.execute('''UPDATE Cars SET Price_3 = 77 WHERE Name = 'Ford' AND 'Tesla' ''')
# conn.commit()


# create tables about of 2 csv with SYM & DATE/PRICE
# join them on their tickers

import pandas as pd 
import sqlite3

cnx = sqlite3.connect('Stocks.db')
c = cnx.cursor()

# df = pd.read_csv('CSVs/07_04_20.csv')
# df.to_sql(name="m07_04_20", con=cnx, index=False)

# df = pd.read_csv('CSVs/07_10_20.csv')
# df.to_sql(name="m07_10_20", con=cnx, index=False)

# df = pd.read_csv('CSVs/07_22_20.csv')
# df.to_sql(name="m07_22_20", con=cnx, index=False)

# conn = sqlite3.connect('Stocks.db')  
# c = conn.cursor()
#         ## make sure the price column doesn't have a NOT NULL constaint
# join_query = '''
# SELECT m07_04_20.*, m07_17_20.*
# FROM   m07_04_20 
#        LEFT JOIN m07_17_20 
#           ON m07_04_20.Ticker = m07_17_20.Ticker
# UNION ALL
# SELECT m07_04_20.*, m07_17_20.*
# FROM   m07_17_20
#        LEFT JOIN m07_04_20
#           ON m07_04_20.Ticker = m07_17_20.Ticker
# WHERE  m07_04_20.Ticker IS NULL
# '''
# data = c.execute(join_query)

# conn = sqlite3.connect('m07_04_20.db')  
# c = conn.cursor()
#         ## make sure the price column doesn't have a NOT NULL constaint
# join_query = '''
# SELECT * FROM m07_04_20
# '''
# data = c.execute(join_query)

# stock_list = []
# for line in data:
#     print(line)
#     stock_list.append(line)

# print(len(stock_list))



# query list of stocks currently in DB
# conn = sqlite3.connect('Stocks.db')
# c = conn.cursor()
# old_list = c.execute('''SELECT Ticker FROM m07_04_20''')
# old_stocks = []
# for line in old_list:
#     stock = str(line).strip("()'',")
#     old_stocks.append(stock)
# print(old_stocks)

# # list of stocks from this week
# old_list = c.execute('''SELECT Ticker FROM m07_10_20''')
# old_stocks_2 = []
# for line in old_list:
#     stock = str(line).strip("()'',")
#     old_stocks_2.append(stock)
# print(old_stocks_2)

# # find the difference
# list_difference = []
# for item in old_stocks_2:
#   if item not in old_stocks:
#     list_difference.append(item)
# list_difference = tuple(list_difference)
# print(list_difference)

# # # query to update 'old ones'
# # query_2 = '''
# # SELECT Ticker, m07_17_20 
# # FROM m07_17_20
# # WHERE Ticker NOT IN (?, ?)
# # '''
# # old_stock_query = c.execute(query_2, list_difference)

# """ Going from here """

# old_stock_query = []

        

# stmt = f"SELECT Ticker, m07_17_20 FROM m07_17_20 WHERE Ticker NOT IN '{sym}'"
# stmt = "SELECT Ticker, m07_10_20 FROM m07_10_20"

# stock = c.execute(stmt)
# old_stock_query.append






# list_4 = []
# for bit in stock:
#     list_4.append(bit)
# list_4 = tuple(list_4)
# print(list_4)

# """ add additional columns with ALTER TABLE __ ADD COLUMN """
# c.execute('''ALTER TABLE m07_04_20 ADD COLUMN m07_17_20''')
# query_3 = '''
# UPDATE m07_04_20
# SET Ticker = 'ALSN' 
# WHERE m07_17_20 = (?)
# '''
# c.executemany(query_3, list_4)
# conn.commit()

# conn = sqlite3.connect('Stocks.db')
# c = conn.cursor()
# c.execute('''ALTER TABLE m07_04_20 ADD COLUMN m07_10_20''')


# stmt = "UPDATE m07_04_20 SET m07_17_20 = '66' WHERE Ticker = 'GTX'"
# c.execute(stmt)
# conn.commit()

# for x, y in list_4:
#     print(f'X - {x}  Y-{y}')
#     stmt = f"UPDATE m07_04_20 SET m07_10_20 = '{y}' WHERE Ticker = '{x}'"
#     c.execute(stmt)
#     conn.commit()
    

# c.execute(stmt)
# conn.commit()







# # first query to insert the new stocks
# query_1 = '''
# SELECT Ticker, m07_17_20 
# FROM m07_17_20
# WHERE Ticker IN (?, ?)
# '''
# new_stock_query = c.execute(query_1, list_difference)

# list_3 = []
# for bit in new_stock_query:
#     list_3.append(bit)
# list_3 = tuple(list_3)
# print(list_3)

# """ add additional columns with ALTER TABLE __ ADD COLUMN """
# c.execute('''ALTER TABLE m07_04_20 RENAME COLUMN m07_17_20 TO m07_17_20''')
#         ### rename column if mistaken
# c.executemany('''INSERT INTO m07_04_20(Ticker, m07_17_20) VALUES(?,?)''', list_3)
# conn.commit()


c.execute('''ALTER TABLE m07_04_20 ADD COLUMN m07_22_20''')

stmt = f"SELECT Ticker, m07_22_20 FROM m07_22_20"
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