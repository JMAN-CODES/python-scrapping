from utils.category_extract import extract_category_data
from utils.scrap_page import scrapper
import json

def subsequent_page():
    
    with open ('pages/home.html','r') as homepage:
        home_page_html = homepage.read()

    sub_pages = extract_category_data(home_page_html)
    
    for page in sub_pages:
        cleaned_page = page.lower().replace(" ","").replace(",","-").replace("ä","ae")
        url = f"https://www.haberkorn.com/{cleaned_page}"
        scrapper(f'category/{cleaned_page}',url)


