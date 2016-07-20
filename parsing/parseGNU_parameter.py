#-*-coding: utf-8-*-

import urllib2
from bs4 import BeautifulSoup
url = 'https://www.gnu.org/software/gsl/manual/html_node/Function-Index.html#Function-Index'
detail = 'https://www.gnu.org/software/gsl/manual/html_node/'

conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a')

f = open("/home/gdm1/바탕화면/GNU_parameter.txt",'w')
total = 0

for tag in links:
    link = tag.get('href',None)
    func_name = tag.find('code')
    if func_name != None :
	func_name = func_name.get_text()
	
	conn = urllib2.urlopen(detail+link)
	html = conn.read()
	soup = BeautifulSoup(html, 'lxml')

	#Search Function
	results = soup.find_all('dt')
        for res in results:
	    res = res.get_text().replace("Function: ","")
	    split = res.split(' ')
	    try:
 	        if func_name == split[0] or func_name == split[1]:
		    total += 1
		    res = res.replace("(","\t").replace(",","\t").replace(")","")
		    f.write(res.replace(u'\xa0',u' ')+"\n")
		    print res
	    except IndexError:
		print "skip"

print total
f.close()
