import pandas as pd
import csv
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
import requests
import time
import re


url =   'https://www.tripadvisor.in/Airline_Review-d8729134-Reviews-Qatar-Airways'

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}

df = pd.read_csv('content_wirte.csv')