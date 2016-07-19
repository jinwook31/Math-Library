import urllib2
from bs4 import BeautifulSoup
url = 'http://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/allclasses-frame.html'
method = 'http://commons.apache.org/proper/commons-math/apidocs/'

conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a')

total = 0

for tag in links:
    link = tag.get('href',None)
    if link is not None:
	conn = urllib2.urlopen(method+link)
	html = conn.read()
	soup = BeautifulSoup(html, 'html5lib')
	
	print link[25:]
	print total

	count = len(soup.find_all('pre'))
	length = range(1,count)

	for i in length:
	    pre = soup.find_all('pre')[i]
	    res = pre.text.replace("\n", "").replace("  ", "")
	    if res[0:2] == 'pu' or res[0] == '@':
	        #print res
		count += 1

	#print "\n"
	total += count

print total
