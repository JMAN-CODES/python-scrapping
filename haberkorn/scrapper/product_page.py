from utils.product_extract import product_extract,indi_prodct_extract
from utils.scrap_page import scrapper
import json
import os
import pandas as pd

def prodcut_page():

    dirs = os.listdir("./pages/category")
    
    for html_page in dirs:
        with open (f'pages/category/{html_page}','r') as page:
            page_html = page.read()
            path_val = os.path.splitext(html_page)[0]

        sub_pages = product_extract(page_html)

        df = pd.DataFrame({
            "name":sub_pages
        })

        df.to_csv(f"data/main_prod/{path_val}.csv")
        

def indi_product():

    dirs = os.listdir("./pages/category")

    for html_page in dirs:
        with open (f'pages/category/{html_page}','r') as page:
            page_html = page.read()
            path_val = os.path.splitext(html_page)[0]

        
        if not os.path.isdir(f'pages/individual_prods/{path_val}'):
            os.mkdir(f'pages/individual_prods/{path_val}')

        sub_pages = product_extract(page_html)
    
        for page in sub_pages:
            cleaned_page = page.lower().replace(" ","").replace(",","-").replace("ä","ae").replace("ü","ue")
            url = f"https://www.haberkorn.com/{path_val}/{cleaned_page}"
            
            scrapper(f'/individual_prods/{path_val}/{cleaned_page}',url)

def extract_subcategory():
    dirs = os.listdir("./pages/individual_prods")
    for page in dirs:
        indi_page = os.listdir(f"./pages/individual_prods/{page}")
        for html_page in indi_page:
            print(html_page)
            with open(f'./pages/category/{page}.html','r') as pagez:
                page_html = pagez.read()
                path_val = os.path.splitext(html_page)[0]
            sub_pages = indi_prodct_extract(page_html,page,path_val)
            
            print("pv:",path_val)
            # if not os.path.isdir(f'pages/individual_prod_prodcuts/{path_val}'):
            #     os.mkdir(f'pages/individual_prods/{path_val}')
            if sub_pages:
                for urls in sub_pages:
                    url = f"https://www.haberkorn.com{urls}"
                    #scrapper()

