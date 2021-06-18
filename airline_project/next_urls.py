import csv
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

#
# def alllinks(intial_links):
#     """
#     This function look for each page next button_only return a csv file with all links
#     :param intial_links: string
#     :return: .csv file containing all links
#     """
#
#     intial_links = input("input string:  ")
#
#     pass
#
#
#
# if __name__ == "__main__":
#     alllinks()


links ="https://www.tripadvisor.in/Airline_Review-d8729004-Reviews-Air-India.html#REVIEWS"
r =  requests.get(links)
soup = BeautifulSoup(r.text, 'html.parser')
data = soup.findAll('div',{ 'class':'page'})
print(data)
# print(link)
