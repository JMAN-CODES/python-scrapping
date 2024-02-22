from utils.scrap_page import scrapper
from utils.regex import job_url_scrap,scrap_job_pages
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed


def indi_job_desc():
    dirs = os.listdir("./pages/job_listing")
    page_list = []
    for page in dirs:
        print(page)
        with open(f'pages/job_listing/{page}','r',encoding="utf8") as indi_page:
            indi_page_content = indi_page.read()
        for all_jobs in job_url_scrap(indi_page_content):
            print(all_jobs)
            # scrapper(f'individual_jobs/{total_job}',all_jobs[0])
            # total_job = total_job+1
        executor = ThreadPoolExecutor(max_workers=5)
        futures = {executor.submit(scrapper, website[-1:-6],website): website for website in all_jobs}
        
        for future in as_completed(futures):
            future()

    

def particular_job_desc():
    dirs = os.listdir("./pages/individual_jobs")
    dataframe = []
    for pages in dirs:
        print(pages)
        with open(f'pages/individual_jobs/{pages}','r',encoding="utf8") as indi_page:
            indi_page_content = indi_page.read()
        dataframe.append(scrap_job_pages(indi_page_content))
    df = pd.DataFrame(dataframe)
    df.to_csv("output.csv")
    

