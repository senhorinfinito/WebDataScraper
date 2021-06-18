
from bs4 import BeautifulSoup
from requests import get
import time
import mmap

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
urls = ['http://economictimes.indiatimes.com/markets/stocks/news', "http://www.business-standard.com/category/markets-news-1060101.htm", "http://www.financialexpress.com/market/"]
output = open("output.txt", "w+")
newest_headline = ["", "", ""]
while(True):
	output.seek(0)
	file_contents = output.read()
	#Economic Times
	ET_page = get(urls[0], headers=hdr)
	ET_soupy = BeautifulSoup(ET_page.content, "html.parser")
	ET_meta = ET_soupy.find_all("meta")
	for meta in ET_meta:
		if(meta.get('itemprop')=='name'):
			content = meta.get('content')
			if(content.find("Latest Stocks in News") == 0):
				continue
			if(file_contents.find(content) != -1):
				continue
			output.write(content+"\n")
	#Business Standard
	BS_page = get(urls[1], headers= hdr)
	BS_soupy = BeautifulSoup(BS_page.content, "html.parser")
	BS_headline_divs = BS_soupy.find_all("div", class_="listing-txt")
	for div in BS_headline_divs:
		for string in div.contents[3].strings:
			if(file_contents.find(string) != -1):
				continue
			output.write(string +"\n")
	#Financial Express
	FE_page = get(urls[2], headers=hdr)
	FE_soupy = BeautifulSoup(FE_page.content, "html.parser")
	FE_h5s = FE_soupy.find_all("h5")
	for h5 in FE_h5s[1:]:
		for string in h5.strings:
			if(file_contents.find(string) != -1):
				continue
			output.write(string+"\n")
	output.flush()
	time.sleep(3)
	print("Woken up.")

