import re
from bs4 import BeautifulSoup
import urllib.request as urllib2

def job_url_scrap(file):
    job_urls = re.findall('<a style="color: #02b44a;" href="(.*?)">\s*(.*?)\s*<\/a>',file,re.S)
    return job_urls

def scrap_job_pages(file):
    job_regex = re.findall('<h2 style="font-size: 20px !important;">\s*(.*?)\s*<\/h2>.*?<a style="color: #333 !important;".*?<\/i>\s*(.*?)<\/a>.*?\s*<i style="color: #02b44a" class="fa fa-black-tie"><\/i>\s*(.*?)\s*<label.*?class="fa fa-money"><\/i>\s*(.*?)p.m.*?<i style="color: #02b44a" class="fa fa-graduation-cap"><\/i>\s*(.*?)\s*<i.*?<i style="color: #02b44a" class="fa fa-map-marker"><\/i>\s*(.*?)<\/div>.*?Gender :\s*(.*?)\s* .*? Age Limit  -\s*(.*?)  .*?Openings - (.*?) Experience - (.*?)Years.*?<div class="title"><a style="color: #02b44a;".*?>(.*?)<\/a><\/div>.*?Posted Date:\s*(.*?)\s*<\/div>.*?Open Until :\s*(.*?)\s*<\/div>.*?<\/ul>(.*?)<a onclick="jobapplylogin',file,re.S)
    return job_regex