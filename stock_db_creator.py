import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('ticker_database.db')  
c = conn.cursor()

# read_clients = pd.read_csv (r'C:\Users\Ron\Desktop\Client\Client_14-JAN-2019.csv')
read_clients = pd.read_csv('07_10_20.csv')
read_clients.to_sql('STOCKS', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'CLIENTS' 

# When reading the csv:
# - Place 'r' before the path string to read any special characters, such as '\'
# - Don't forget to put the file name at the end of the path + '.csv'
# - Before running the code, make sure that the column names in the CSV files match with the column names in the tables created and in the query below
# - If needed make sure that all the columns are in a TEXT format

c.execute('''
INSERT OR IGNORE INTO STOCKS (Ticker,07_10_20)
          ''')

# c.execute('''
# SELECT DISTINCT *
# FROM DAILY_STATUS
# WHERE Date = (SELECT max(Date) FROM DAILY_STATUS)
#           ''')
   
#print(c.fetchall())

df = DataFrame(c.fetchall(), columns=['Ticker','07_10_20'])
print (df) # To display the results after an insert query, you'll need to add this type of syntax above: 'c.execute(''' SELECT * from latest table ''')

df.to_sql('STOCKS', conn, if_exists='append', index = False) # Insert the values from the INSERT QUERY into the table 'DAILY_STATUS'

# export_csv = df.to_csv (r'C:\Users\Ron\Desktop\Client\export_list.csv', index = None, header=True) # Uncomment this syntax if you wish to export the results to CSV. Make sure to adjust the path name
# Don't forget to add '.csv' at the end of the path (as well as r at the beg to address special characters)