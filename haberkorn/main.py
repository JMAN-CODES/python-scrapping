import sys
from scrapper.main_page import main_page_scrapper
from scrapper.subsequent_pages import subsequent_page
from scrapper.product_page import prodcut_page,indi_product,extract_subcategory
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
            elif sys.argv[2] == 'sub_page':
                subsequent_page()
            elif sys.argv[2] == 'product_extract':
                prodcut_page()
            elif sys.argv[2] == 'indi_product':
                indi_product()
            elif sys.argv[2] == 'subcategory':
                extract_subcategory()
            elif sys.argv[2] == 'all':
                main_page_scrapper()
                subsequent_page()
                prodcut_page()
                indi_product()
            else:
                print("command not recogonized")
        except Exception as e:
            print(e)
    else:
        print("args not recogonized!")
