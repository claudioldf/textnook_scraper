import re
import sys
import urllib2

"""
extracts the titles from entry-title class
regular expression [^>] means all except symbol '> or until '> is reached 
"""
def extract_title(pageContent):
	title_extract = []
	title_match = re.findall(r'entry-title"><[^>]+>([^<]+)', pageContent)
	
	for raw_title in title_match:	
		raw_title = re.sub(re.escape('&nbsp;'), ' ', raw_title)
		title_extract.append(raw_title)
	#stray string &nbsp: removed from all titles
	return title_extract	

"""
extracts the dates from entry-date class
regular expression [^>] means all except symbol '> or until '> is reached 
"""
def extract_date(pageContent):
	date_match = re.findall(r'"entry-date"[^>]+>([^<]+)', pageContent)
	
	return date_match
"""
extracts urls of all articles 
so that they can be accessed individually and proceesed
for extracting likes and comments in case which are zero in this case
""" 
def extract_links(pageContent):
	link_match = re.findall(r'entry-title"><a\shref="([^"]+)"', pageContent)
	return link_match

def main():
	url = 'https://textnook.wordpress.com/'
	response = urllib2.urlopen(url)
	webContent = response.read()
	#webContent contains the webpage as a string
	f = open('solution.txt', 'w')

	titles = extract_title(webContent)[:]
	for title in titles:
		f.write(title + '\n')

	dates = extract_date(webContent)[:]
	for date in dates:
		f.write(date + '\n')

	#extract_links(webContent)
	f.close()

if __name__ == '__main__' : main()
