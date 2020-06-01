# Importing libraries and modules
from bs4 import BeautifulSoup
import requests

# Global variables 
url = " "
count = 0
list_of_urls = []
list_of_words = []
extract = ""


# This is an iterative function which takes a URL as an argument and iterates through each page it can lead to further
def webCrawler(URL):
    r  = requests.get(URL)
    data = r.text
    global count
    soup = BeautifulSoup(data, features="html.parser")
    for link in soup.find_all('a'):
        link_extracted = link.get('href')
        if link_extracted in list_of_urls:
        	continue
        elif link_extracted == '#':
            continue
        if link_extracted == None:
        	continue
        elif link_extracted == '/':
            continue
        elif link_extracted[0] == "#":
        	continue
        elif link_extracted[:4] == "http":
            if extract not in link_extracted and link_extracted != url:
                continue
            else:
            	if link_extracted in list_of_urls:
            		continue
            	else:
            		list_of_urls.append(link_extracted)
            		print(link_extracted)
            		count = count + 1
            		webCrawler(link_extracted)
        elif link_extracted[0] == "/":
        	link_extracted = URL + link_extracted
        	if link_extracted in list_of_urls:
        		continue
        	else:
        		list_of_urls.append(link_extracted)
        		count = count + 1
        		print(link_extracted)
        		webCrawler(link_extracted)
        else:
            if link_extracted in list_of_words:
                continue
            list_of_words.append(link_extracted)
            link_extracted = URL + "/" + link_extracted
            link_extracted1 = url + "/" + link_extracted
            if link_extracted1 not in list_of_urls:
                if link_extracted in list_of_urls:
                    continue
       	        else:
                    list_of_urls.append(link_extracted)
                    count = count + 1
                    print(link_extracted)
                    webCrawler(link_extracted)


# Asking user to input the websites URL
url = input("Enter a website to extract the URL's from: ")
if url[0:5] == "https":
    extract = url[13:len(url)]
elif url[0:4] == "http":
    extract = url[12:len(url)]
webCrawler(url)

# Making html files of the whole website in the same directory as this file
count = 0
for Url in list_of_urls:
    r = requests.get(Url)
    with open('page'+ str(count) + '.html', 'w') as func:
        func.write(r.text)
        count = count + 1
