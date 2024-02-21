import requests
from bs4 import BeautifulSoup
sess = requests.session()
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    # "Cookie": "ASP.NET_SessionId=aamoss55vyccddyzy5y30m45; cookiesession1=678B288E843E047E02F130FF59E49A40",
    "Host": "cado.eservices.gov.nl.ca",
    "Origin": "https://cado.eservices.gov.nl.ca",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0"
}
 
url='https://cado.eservices.gov.nl.ca/CadoInternet/Main.aspx'
x = sess.get(url, headers=headers)
html_content=x.text

viewstate = re.search('"__VIEWSTATE"\svalue="(.*?)"',html_content,re.S)

viewstate_input = viewstate.group(1)

#soup = BeautifulSoup(html_content, 'html.parser')

# Find the input tag with name '__VIEWSTATE'
# viewstate_input = soup.find('input', {'name': '__VIEWSTATE'})
 
# Check if the input tag is found and extract its value
 
x=sess.get('https://cado.eservices.gov.nl.ca/CadoInternet/Company/CompanyMain.aspx')
 
params = {
    "__VIEWSTATE": viewstate_input,
    "txtNameKeywords1": "AAA",
    "txtNameKeywords2": "",
    "txtCompanyNumber": "",
    "btnSearch.x": "56",
    "btnSearch.y": "13"
}
 
 
x = sess.post ('https://cado.eservices.gov.nl.ca/CadoInternet/Company/CompanyNameNumberSearch.aspx', headers=headers,data=params)
 
with open('table.html','w') as fs:
    fs.write(x.text)