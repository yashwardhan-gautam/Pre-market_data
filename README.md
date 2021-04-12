## Pre-market_data
Scrapping pre-market data of Nifty 50 using Selenium in Python

### Dependencies 
[Chrome Drivers](https://chromedriver.chromium.org/)  
[Selenium](https://pypi.org/project/selenium/)  
[beautifulsoup4](https://pypi.org/project/beautifulsoup4/)  
[pandas](https://pypi.org/project/pandas/)  

### How to Run ?
python3 scrapper.py

### What else 
In case the layout of the website and/or the positions, number of columns of the table changes the corresponding changes have to be 
made in the code as well
Apart from reading as CSV file, we can make the chrome drivers directly click on the download CSV button on the website as well to download the CSV, everytime.
Other than this, one can make the driver hover on the Nifty 50 section to extract other CSV files (for Nifty Bank, F&O etc.).
