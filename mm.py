import requests
from bs4 import BeautifulSoup
url="http://whatismyip.host/"
page=requests.get(url,headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"})
#print(page.text)
soup = BeautifulSoup(page.text,'html.parser')
ip_address_list= soup.find(class_='ipaddress')
print(ip_address_list)


















