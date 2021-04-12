import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market"
driver = webdriver.Chrome()
driver.get(url)
import time
time.sleep(10)

action = ActionChains(driver)

# live_market_section = driver.find_element_by_xpath('//*[@id="MAKRET_DATA"]/a')
# action.move_to_element(live_market_section).perform()

# equity_derivatives = driver.find_element_by_xpath('//*[@id="Pre-Open_Market"]/a')
# equity_derivatives.click()

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
time.sleep(7)

result = soup.find('table',{'id': 'livePreTable'})
table_rows = result.find_all('tr')

l = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
    
# Creating the table using pandas
equity_derivatives_table = pd.DataFrame(l, columns=["+","Symbol","Prev_Close","IEP_Price","Chng",
                                 "%Chng","Final_Price","Final_Quantity","Value(lakhs)",
                                 "FFM_CAP(lakhs)","NM 52W H","NM 52W L", "TODAY"])

equity_derivatives_table = equity_derivatives_table.drop([0], axis=0)

equity_derivatives_table

equity_derivatives_table.to_csv("Pre-market-watch-Nifty_50.csv", index=0)
