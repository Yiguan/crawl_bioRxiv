# download bioRxio 
# python3

from Cookie2Dict import cookie2dict
import requests
import re
from bs4 import BeautifulSoup

class getBio:
	'''set cookies and headers,
	and return a page source code'''
	def __init__(self,url):
		self.url = url
	def cookies(self,cookies_string):
		convert = cookie2dict(cookies_string)
		self.cookies_string = convert.ToDict()
		#return self.cookies_string
	def header(self, header_string):
		key = header_string.split(":")[0]
		value = header_string.split(":")[1].strip()
		aa = {key:value}
		self.header_string = aa
		#return self.header_string
	def getContent(self,page):
		rr = requests.get(self.url+str(page), headers = self.header_string, cookies = self.cookies_string)
		try:
			return rr.text
		except Exception as error:
			print("Page Error!")

# set cookies 
my_cookie = "__cfduid=d47b03f9bf519ef3de0d0f7ce8e0f56eb1557707853; _ga=GA1.2.556283552.1557707858; SSESS1dd6867f1a1b90340f573dcdef3076bc=NJhH0EXmZj4Odka5zOZ1ODC-SS2NXK8-KwdG0VXDlQY; SESS1dd6867f1a1b90340f573dcdef3076bc=Smw6OMsGhZYu-6tsVxHd6SksX5Vg2OrxFuHJMM6iANU; has_js=1; _gid=GA1.2.1265091862.1559864442; cookie-agreed=2"
# set headers
my_header = "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
# initiate getBio class
my_py = getBio("https://www.biorxiv.org/content/early/recent?page=")
my_py.cookies(my_cookie)
my_py.header(my_header) 

# Loop pages to download info.
regex = re.compile('highwire-article-citation highwire-citation-type-highwire-article tooltip-enable')
my_date = []
my_title = []
# from the first page to last page
# parse page
for p in range(1,5139):
	print(p)
	p_src = my_py.getContent(p)
	my_soup = BeautifulSoup(p_src,"html.parser")
	for p_list in my_soup.find_all('div', attrs = {'class':regex}):	
		p_date = "_".join(p_list['data-apath'].split("/")[3:6])
		p_title = p_list.find("span", attrs = {'class':'highwire-cite-title'}).text.strip()
		my_date.append(p_date)
		my_title.append(p_title)


import pandas as pd
my_pd = pd.DataFrame(list(zip(my_date, my_title)), columns = ["date","title"])
my_pd.to_csv("biorxiv.csv", index = None, header = True)











