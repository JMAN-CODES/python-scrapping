from utils.scrap_page import scrapper
from utils.regex import job_url_scrap,scrap_job_pages
import os
from bs4 import BeautifulSoup
import urllib.request as urllib2
from collections import defaultdict 
import pandas as pd
import logging

def indi_job_desc():
    dirs = os.listdir("./pages/job_listing")
    
    total_job = 0
    for page in dirs:
        print(page)
        with open(f'pages/job_listing/{page}','r',encoding="utf8") as indi_page:
            indi_page_content = indi_page.read()

        for all_jobs in job_url_scrap(indi_page_content):
            print(all_jobs)
            scrapper(f'individual_jobs/{total_job}',all_jobs[0])
            total_job = total_job+1

def particular_job_desc():
    dirs = os.listdir("./pages/individual_jobs")
    dataframe = []

    for pages in dirs:
        print(pages)
        job_desc = defaultdict(str)
        
        # url = f'pages/individual_jobs/{pages}'
        with open(f'pages/individual_jobs/{pages}','r',encoding="utf8") as indi_page:
            indi_page_content = indi_page.read()
        soup = BeautifulSoup(indi_page_content,'html5lib')

        
        table = soup.find('div', attrs = {'class':'location'})
        money = soup.find('div', attrs = {'style':'font-size: 15px;line-height: 20px;'})
        company = soup.find('div', attrs = {'class':'title'})
        title = soup.find('h2', attrs = {'style':'font-size: 20px !important;'})
        #print(table,title,company,money)

        for row in title:
            logging.debug(row.text.strip().replace(" ",""))
            job_desc['title'] = row.text.strip().replace(" ","")
        for row in company:
            logging.debug(row.text.strip().replace(" ",""))
            job_desc['name'] = row.text.strip().replace(" ","")
        for row in money:
            logging.debug(row.text.strip().replace(" ",""))
            job_desc['city'] = row.text.strip()
        for row in table:
            logging.debug(row.text.strip().replace(" ",""))
            job_desc['desc'] = row.text.strip()
        dataframe.append(job_desc)
    df = pd.DataFrame(dataframe)

    df.to_csv("output.csv")
    

