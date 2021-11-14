import numpy as np
from bs4 import BeautifulSoup
from requests import get
import  timeit
pages = np.arange(1, 2, 1)
start = 1
end = 223
data = []
url_list =[]

def all_urls(start, end):
    with open('urls.txt', 'w') as file:
        for pagenumber in range(start, end):
            url = f'https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={pagenumber}'
            data = get(url)
            soup = BeautifulSoup(data.content, 'html.parser')
            links = soup.find_all('a', attrs= {"class":"_1fQZEK"})
            for item in links:
                main_url = 'https://www.flipkart.com'
                sub_url = item.get('href')
                data_url = main_url + sub_url
                file.write(data_url)
                file.write('\n')
            print(f'{pagenumber}')
    file.close()
time_start = timeit.default_timer()
print('time start')
(all_urls(start, end))
time_end = timeit.default_timer()
print("total time taken:  ", time_end -  time_start)