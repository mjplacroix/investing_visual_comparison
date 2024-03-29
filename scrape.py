# remeber to start/load pip environment
# > pipenv shell

import webbrowser as wb
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import date

browser = webdriver.Firefox()
type(browser)
browser.get('https://www.magicformulainvesting.com/Account/LogOn')
user_element = browser.find_element_by_id('Email')
user_element.send_keys('michael.jp.lacroix@gmail.com')
password_element = browser.find_element_by_id('Password')
password_element.send_keys('mCqB0bbC2JJqEm')

linkElem = browser.find_element_by_id("login")
linkElem.click()

linkElem = browser.find_element_by_id('stocks')
linkElem.click()

tickers = []
for i in range(1, 31):
    # error appeared on this line on 11-27-20  # did NOT occur the next week 12-04-20
    # error on 4-2-21 -- temp fix by changing range to (2, 31), running, then changing back
    ticker = browser.find_element_by_xpath(f'/html/body/div[1]/div[4]/div/div[1]/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/table/tbody/tr[{i}]/td[2]').text
    tickers.append(ticker)
# take in a string

print(tickers)

# iterate through the entire string 
for ticker in tickers:
    print(ticker)


today = date.today()
d3 = today.strftime("%m_%d_%y")

with open(f'{d3}.csv', 'w') as stock_list:
    for ticker in tickers:
        stock_list.write('%s\n' % ticker)


# with open('testing_2.csv', mode='w') as magic_form_stocks:
#     magic_formula = csv.writer(magic_form_stocks, delimiter=',')

#     magic_formula.writerow([tickers])



# opening the csv file in 'w+' mode 
file = open('g4g.csv', 'w+', newline ='') 
  
# writing the data into the file 
with file:     
    write = csv.writer(file) 
    write.writerows(tickers) 