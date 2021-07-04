import csv
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

pages = np.arange(1, 31, 1)

data = []
for page in pages:
    page_link = requests.get(f'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}')
    soup = BeautifulSoup(page_link.content, 'html.parser')
    laptops_info = soup.find_all('div', attrs = {'class': '_3pLy-c row'})

    for item in laptops_info:
        try:
            laptop_info = {'Laptop Name': item.find('div', attrs = {'class': '_4rR01T'}).text,
                           'Price': item.find('div', attrs = {'class': '_30jeq3 _1_WHN1'}).text,
                           'Overall Rating': item.find('div', attrs = {'class': '_3LWZlK'}).text,
                           'Total Ratings': item.find('span', attrs = {'class': '_2_R_DZ'}).text.split('&')[0],
                           'Total Reviews': item.find('span', attrs = {'class': '_2_R_DZ'}).text.split('&')[1],
                           'Processor': item.find('ul', attrs = {'class': '_1xgFaf'}).find_all('li')[0].text,
                           'RAM': item.find('ul', attrs = {'class': '_1xgFaf'}).find_all('li')[1].text,
                           'OS': item.find('ul', attrs = {'class': '_1xgFaf'}).find_all('li')[2].text,
                           'Storage': item.find('ul', attrs = {'class': '_1xgFaf'}).find_all('li')[3].text,
                           'Screen': item.find('ul', attrs = {'class': '_1xgFaf'}).find_all('li')[4].text,
                           'Warranty': item.find('ul', attrs = {'class': '_1xgFaf'}).find_all('li')[5].text}
            data.append(laptop_info)

        except:
            pass
    print(f'Page: {page}')

laptop_details =  pd.DataFrame(data = data)
laptop_details.to_csv('laptop_details_output.csv')