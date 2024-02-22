from utils.scrap_page import scrapper
from utils.regex import job_url_scrap,scrap_job_pages
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, wait
from queue import Queue, Empty


def indi_job_desc():
    dirs = os.listdir("./pages/job_listing")
    data_queue = Queue()
    for page in dirs:
        #print(page)
        data_queue.put(page)
    
    print(data_queue.qsize())
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(_worker,data_queue) for _ in range(10)]
        wait(futures,timeout=None)

def _worker(data_queue):
    while True:
        try:
            page = data_queue.get_nowait()
            print(page)
            with open(f'pages/job_listing/{page}','r',encoding="utf8") as indi_page:
                indi_page_content = indi_page.read()
                for all_jobs in job_url_scrap(indi_page_content):
                    name = all_jobs[-5::]
                    scrapper(f'individual_jobs/{name}',all_jobs)
        except Empty:
            break

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
    

