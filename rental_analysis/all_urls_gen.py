import pandas as pd
from bs4 import BeautifulSoup
from requests import get
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url_list = []
def all_urls(start, end):
    for pagenumber in range(start, end):
        url = f'https://www.99acres.com/property-for-rent-in-pune-ffid-page-{pagenumber}'
        data = get(url, headers = hdr)
        soup = BeautifulSoup(data.content, 'html.parser')
        links = soup.find_all('a', attrs= {"class":"body_med srpTuple__propertyName"})
        for item in links:
            main_url = 'https://www.99acres.com'
            sub_url = item.get('href')
            data_url = main_url + sub_url
            url_list.append(data_url)
        print(f'pages {pagenumber}')
    return (url_list)

urls = (all_urls(1,5))
datadetail = pd.DataFrame(urls)
datadetail.to_csv('all_urls.txt')