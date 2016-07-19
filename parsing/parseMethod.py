#-*-coding: utf-8-*-

import urllib2
from bs4 import BeautifulSoup
url = 'http://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/allclasses-frame.html'
method = 'http://commons.apache.org/proper/commons-math/apidocs/'

conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a')

f = open("/home/gdm1/바탕화면/apache_commons.txt",'w')

total = 0

for tag in links:
    link = tag.get('href',None)
    if link is not None:
	conn = urllib2.urlopen(method+link)
	html = conn.read()
	soup = BeautifulSoup(html, 'html5lib')
		
	count = len(soup.find_all('pre'))
	length = range(1,count)
	res = ""

	#Get Method to String
	for i in length:
	    pre = soup.find_all('pre')[i]
	    tmp = pre.text.replace("\n", "").replace("  ", "")

	    if tmp[0:2] == 'pu':
	        res = tmp

	    if tmp[0:17] == '@Deprecatedpublic':
		res = res.replace("@Deprecatedpublic","public")
		tes = tmp

	    if res != "":
        	write = link[25:len(link)-5]+"\t"+res.replace(",","\t").replace("(","\t")
		index = write.rfind(')')
		write = write[0:index]
		print write
		f.write(write.replace(u'\xa0', u' ')+"\n")
		total += 1
		res = ""

print total
f.close()
