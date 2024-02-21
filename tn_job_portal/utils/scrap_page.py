import logging
import requests

def scrapper(name,page_url):
    logging.info(f"scrapping {page_url}")
    sess = requests.session()
    page = sess.get(page_url)

    with open(f'pages/{name}.html','w',encoding="utf-8") as pg:
        pg.write(page.text)

    logging.info(f'scrapped {page_url} as saved as html')
