# coding: utf-8
import bs4
url='http://www.cwb.gov.tw/V7/index.htm'
from urllib.request import urlopen
soup = bs4.BeautifulSoup(urlopen(url), 'lxml')
#print(soup)
link = soup.findAll('a', href=True)
for i in link:
	#print('{}\t{}'.format(i.string, i))
	print(i.string)
print("Total Link: {}".format(len(link)))
#soup.findAll('input')
