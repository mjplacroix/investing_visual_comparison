

import webbrowser as wb
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd


browser = webdriver.Firefox()
type(browser)
browser.get('https://www.edwardjones.com/us-en/search/financial-advisor/results?query=07666&distance=5000&page=1&view=list')



bit = browser.find_element_by_xpath(f'/html/body/div[1]/main/div[3]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/ul/li[1]/div/div[1]/div[2]/div[1]')

print(bit)