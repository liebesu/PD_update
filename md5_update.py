import MySQLdb
import os
import re
import urllib
from bs4 import BeautifulSoup
import requests
from urlparse import urljoin
__author__ = 'liebesu'
def malshare():
    url='http://malshare.com/daily/'
    r=requests.get(url)
    s=BeautifulSoup(r.text,"html.parser")
    for link in s.find_all('a'):
        relurl=urljoin(url,link.get('href'))
        r=requests.get(relurl)
        s=BeautifulSoup(r.text,"html.parser")
        for link in s.find_all(href=re.compile("^malshare_fileList")):
            relurl=urljoin(relurl,link.get('href'))
            if os.path.exists("malshare"):
                pass
            else:
                os.makedirs("malshare")
            filepath=os.path.join(os.getcwd(),"malshare")
            print filepath
            urllib.urlretrieve(relurl,os.path.join(filepath,link.get('href')))
def virusshare():
    url='https://virusshare.com/hashes/'
    r=requests.get(url)
    r.content

def check_md5():
     mysql
