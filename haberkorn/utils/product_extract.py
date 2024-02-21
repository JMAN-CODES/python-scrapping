import re

def product_extract(file):
    prod_data = re.findall('<div class="h4">(.*?)\<',file,re.S)
    return prod_data

def indi_prodct_extract(file,main,sub):
    prod_data = re.findall(f'class="dropdown-item" href="(\/{main}\/{sub}\/.*?)"',file,re.S)
    return prod_data