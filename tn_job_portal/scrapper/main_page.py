from utils.scrap_page import scrapper

def main_page_scrapper():

    for i in range(0,351,10):
        scrapper(f'page{i}',f'https://www.tnprivatejobs.tn.gov.in/Home/jobs/{i}')