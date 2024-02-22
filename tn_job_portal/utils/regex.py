import re
from bs4 import BeautifulSoup
import urllib.request as urllib2
from collections import defaultdict 
import logging

def job_url_scrap(file):
    job_urls = re.findall('<a style="color: #02b44a;" href="(.*?)">',file,re.S)
    return job_urls

def scrap_job_pages(file):
    
    job_desc = defaultdict(str)
    soup = BeautifulSoup(file,'html5lib')
    table = soup.find('div', attrs = {'class':'location'})
    money = soup.find('div', attrs = {'style':'font-size: 15px;line-height: 20px;'})
    company = soup.find('div', attrs = {'class':'title'})
    title = soup.find('h2', attrs = {'style':'font-size: 20px !important;'})
    money_page = 0

    for row in title:
        logging.debug(row.text.strip().replace(" ",""))
        job_desc['title'] = row.text.strip().replace(" ","")
    for row in company:
        logging.debug(row.text.strip().replace(" ",""))
        job_desc['name'] = row.text.strip().replace(" ","")
    for row in money:
        logging.debug(row.text.strip().replace(" ",""))
        text = row.text.strip().replace(" ","")
        if (text == ''):
            pass
        else:
            pattern = r'\b\w+\b'
            matches = re.findall(pattern, text)
            extracted_text = ' '.join(matches)
            job_desc['city'] = row.text.strip()
            if money_page == 0:
                job_desc['money'] = extracted_text
            elif money_page == 1:
                job_desc['requirements'] = extracted_text
            else:
                job_desc['location'] = extracted_text
            print(extracted_text.split())
            money_page += 1
    return job_desc