import re

def extract_category_data(file):
    cat_data = re.findall('data-ga-label=\"(.*?)\" title.*?>',file,re.S)
    cat_data.pop()
    return cat_data
    