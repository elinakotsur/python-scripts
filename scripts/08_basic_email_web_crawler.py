from bs4 import BeautifulSoup
import requests

# get url
url = input('Enter a URL (include `http://`): ')
response = requests.get(url)
html=response.text
print(html)


soup=BeautifulSoup(html,"html.parser")
# print the number of links in the list


    
link = []
for i in soup.find_all("a",href=True):
    link.append(i)
    print("leidnut link:",i)
