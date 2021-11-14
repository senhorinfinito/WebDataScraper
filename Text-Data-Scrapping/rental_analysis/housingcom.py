""""THis is a basic scrapper tool design to scrap housing renatal data from housing.com
In this project we are going to scraping
1. area in sq. ft.,
2. property size in BHK,
3. reantal price,
4. Sub area,
5. City region,
6. house contion:  unfurnished / furnished
7. basic details/desciption  of house,
8. owner & broker info
9. trusted agent
10 . Owner verification """
import pandas as pd
import requests

""" Import required libraries """

from bs4 import BeautifulSoup
from requests import get

list_data =[]
for i in range(1,1240):
    url = f'https://housing.com/rent/flats-for-rent-in-pune-maharashtra-P2r4v3l939lxd541t?page={i}'

    data = get(url)
    soup = BeautifulSoup(data.content, 'html.parser')

    housing_data = soup.find_all('article', attrs= {"class":"css-8jw9t9"})

    for item in housing_data:

        """ Verification ID"""
        try:
            verification = item.find('div', attrs = {'class':'css-105wb3r'}).text
        except:
            verification = 'Not verified'

        """ Rent prices """
        try:
            rent =item.find('div', attrs = {"class":"css-1cxwewr"}).text
        except:
            house_details = 'Not available'

        """Home details"""
        try :
            bhk = item.find('div', attrs = {"class":"css-ybv4ci"}).text
        except:
            bhk = 'Not avaiable'

        """Address"""
        try :
            area = item.find('div', attrs = {"class":"css-1o3sqfg"}).text
        except:
            area = 'Not provided'

        """Features"""
        try:
            feature = item.find('div', attrs={"class": "css-14teu4h"}).text
        except:
            feature = 'Not provided'

        """Details Task"""

        try:
            description = item.find('div', attrs={"class": "css-3jzye6"}).text
        except:
            description = 'Not provided'


        """Listing details"""

        try:
            listing = item.find('div', attrs={"class": "certified-highlights css-8k1gqd"}).text
        except:
            listing = 'Not provided'



        house_details = {'isverified': verification, 'rent prices': rent, 'home_details': bhk, "area": area, 'feature': feature,
                         'description': description, "listing":listing}
        list_data.append(house_details)

    print(f'page = {i}')
    # time.sleep(1)

all_data = pd.DataFrame(list_data)
all_data.to_csv('rental.csv')

