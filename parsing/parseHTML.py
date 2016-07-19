import urllib2
from bs4 import BeautifulSoup
url = 'http://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/allclasses-frame.html'
method = 'http://commons.apache.org/proper/commons-math/apidocs/'

conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a')

for tag in links:
    link = tag.get('href',None)
    if link is not None:
	#xconn = urllib2.urlopen(method+link)
	#html = conn.read()
	#soup = BeautifulSoup(html, 'lxml')
	print method+link
    
