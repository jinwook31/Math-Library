import urllib2
from bs4 import BeautifulSoup
url = 'http://commons.apache.org/proper/commons-math/apidocs/org/apache/commons/math3/fitting/WeightedObservedPoint.html'

conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html, 'html5lib')

count = len(soup.find_all('pre'))
length = range(1,count)

for i in length:
   pre = soup.find_all('pre')[i]
   res = pre.text.replace("\n","").replace(" ","")
   if res[0] == 'p':
	print 'true'
