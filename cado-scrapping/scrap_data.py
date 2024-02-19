import requests
from const_val import HEADERSZ

sess = requests.session()

first_page = sess.get('https://cado.eservices.gov.nl.ca/CADOInternet/Main.aspx',headers=HEADERSZ)

with open("first_page.html",'wb') as fp:
    fp.write(first_page.content)