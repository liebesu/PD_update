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
    for link in s.find_all(href=re.compile('\d')):
        datapath=os.path.join("malshare", link.get('href'))
        if os.path.exists(datapath):
            pass
        else:
            os.makedirs(datapath)
            relurl = urljoin(url, link.get('href'))
            r = requests.get(relurl)
            s = BeautifulSoup(r.text, "html.parser")
            for link in s.find_all(href=re.compile("^malshare_fileList")):
                relurl=urljoin(relurl,link.get('href'))
                filepath=os.path.join(os.getcwd(),datapath)
                print "Downloading..",relurl
                urllib.urlretrieve(relurl,os.path.join(filepath,link.get('href')))
    print "Malshare download finished"
def virusshare():
    url='http://virusshare.com/hashes/'
    r=requests.get(url)
    s=BeautifulSoup(r.content,"html.parser")
    links=s.find_all(href=re.compile('^VirusShare'))
    if os.path.exists("virusshare"):
        pass
    else:
        os.makedirs("virusshare")
    for link in links:
        filepath = os.path.join("virusshare", link.get('href'))
        realurl=urljoin(url,link.get('href'))
        if os.path.exists(filepath):
            pass
        else:
            print "virusshare downloading ",link.get('href')
            urllib.urlretrieve(realurl,filepath)
    print "virusshare download finish"

def db_refine():
    if os._exists("refine"):
        pass
    else:
        os.makedirs("refine")

def check_md5():
    db = MySQLdb.connect(host='192.168.25.62', db='pd_update', user='root', passwd='polydata', port=3306,
                         charset='utf8')
    cursor = db.cursor()
    try:
        select_sql='select md5 from MD5 into outfile "/var/lib/mysql-files/md5_all"'

if __name__=="__main__":
     malshare()
     virusshare()
