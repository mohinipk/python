import requests
from bs4 import BeautifulSoup
url="http://whatismyip.host/"
page=requests.get(url,headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"})
#print(page.text)
soup = BeautifulSoup(page.text,'html.parser')
ip_address_list= soup.find(class_='ipaddress')
#print(ip_address_list)

m=str(ip_address_list)
fhand=open('k.txt','w')
fhand.write(m)


cat k.txt | grep -oE "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*" #this command works in command promt



















