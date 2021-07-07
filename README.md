![alt text](https://github.com/senhorinfinito/scrappers/blob/main//data_scrapper.png?raw=true)


![Visitor Count](https://profile-counter.glitch.me/{senhorinfinito}/count.svg)


## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# Web Scraping using Python
While working on existing datasets, I feel that these datasets are best for brushing up data cleaning, feature engineering skills. But the working on a brand new data set has always felt incomplete.  So I learned web scraping by using Python.  BeautifulSoup is a python library is helps you to web scrap tasks very efficiently & easily.  

These are projects which I have done in web data scrapping:

## Housing Rental Prices.  - [code](https://github.com/senhorinfinito/scrappers/blob/main/rental_analysis/99acres.py)

This code helps you to find different house's data which is the available web. 

I preferred 99acres.com for this project. The interface of the web page looks like this:

![99acre.com](https://github.com/senhorinfinito/scrappers/blob/main/images/99acres.jpg)

Run the web scraper to scrape 15000 housing data from [99acres.com](https://www.99acres.com/flats-for-rent-in-pune-ffid-page-2) Each sample(row) has the following points:
- rent (Target Variable)
- Number of bedrooms
- Number of bathrooms 
- Number of Balconies 
- Brokerage amount 
- Deposit Amount 
- Maintenance amount
- Built-Up Area
- Super Built-Up Area
- Type of Furnishing
- Availability for 
- Address
- Floor Number 
- Home Facing
- Floor-type
- Gate Community
- Corner Property 
- Parking Count
- WheelChairFacility
- Pet-Friendly
- Agreement Duration
- Electricity Bill
- Power Backup  Facility
- Property age
 



## Housing Rental from [Housing.com](https://housing.com/rent/flats-for-rent-in-pune-maharashtra-P2r4v3l939lxd541t?page=1) 

This is my first python web scrapping learning project.

I have used [housing.com](https://housing.com/rent/flats-for-rent-in-pune-maharashtra-P2r4v3l939lxd541t?page=1) for this project & managed  to collect following points for a house. 
 
 
![image](https://github.com/senhorinfinito/scrappers/blob/main/images/housing.com.jpg)

 - Rent
 - BHK 
 - Area
 - Hightlighted Features 
 - Text Description 
 - Verification status
 - Facility Listing 
 
This helps you to scrap around 6000 homes data.  

Here you can check for [code](https://github.com/senhorinfinito/scrappers/blob/main/rental_analysis/housingcom.py)


##  Laptop Data Scrapping With Specifications. 

Every E-commerce website is a data repository. This repository helps you t get laptops & their specifications. It is capable of scrapping 470+ laptops data from [filpkart.com](https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off). 

![image](https://github.com/senhorinfinito/scrappers/blob/main/images/laptop_details.jpg)
This code returns the following details:
1. Laptop Name
2. Price -  Target
3. Overall rating
4. Total reviews
5. Total rating
6. Processor
7. RAM
8. OS 
9. Storage 
10. Screen Size
11. Warranty 
12. Accessory 

Here you can check the [code](https://github.com/senhorinfinito/scrappers/blob/main/laptop_details/scrapper.py).

Suggestions: If you want to scrap more data quantity please use more exceptions.


## Stock Market News Scrapping.

This scraper helps to scrap the text of each headline from India's top newspaper websites.  

I preferred the following newspapers websites for data collection: 

1. Economics Times 
2. Financial Express
3. Business Standard

you can check the output file [here](https://github.com/senhorinfinito/scrappers/blob/main/news_headings/scrapper%20combined.py)

This input code will be utilized for more data collection & update on django_server for the upcoming NLP project.


## Telegram group communication history: JSON File

Every Telegram chat can be exported into a JSON file. This project helps to scraps chat text data as well as know more about actions inside a group, warning messages & user info.


I Have owned three groups that contain various topics discussions, I have stored that file in the local repository. This code helps you scrap 75000  chat history in 1.05  sec.  

Here you can check the code for more [details](https://github.com/senhorinfinito/scrappers/blob/main/telegram_chat/telegram_chat_history_json.py). 
