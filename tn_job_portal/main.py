import sys
from scrapper.main_page import main_page_scrapper
from scrapper.indi_job_pages import indi_job_desc,particular_job_desc
import logging
import json
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


if __name__ == '__main__':
    
    if sys.argv[1] == 'scrap':
        try:
            if sys.argv[2] == 'main':
                main_page_scrapper()
            elif sys.argv[2] == 'indi_job_desc':
                indi_job_desc()
            elif sys.argv[2] == 'scrap_jobs':
                particular_job_desc()
            # elif sys.argv[2] == 'product_extract':
            #     prodcut_page()
            # elif sys.argv[2] == 'indi_product':
            #     indi_product()
            # elif sys.argv[2] == 'subcategory':
            #     extract_subcategory()
            elif sys.argv[2] == 'all':
                main_page_scrapper()
                indi_job_desc()
                particular_job_desc()
                
            else:
                print("command not recogonized")
        except Exception as e:
            print(e)
    else:
        print("args not recogonized!")
