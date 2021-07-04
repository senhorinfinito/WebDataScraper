import scrapy_tripadvis as st
import pandas as pd

path = r"C:\Users\Anant Sakhare\Desktop\scrapper\airline_project\chromedriver.exe"

df = st.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)