import MySQLdb
import os
import re
import urllib

import time
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
    print "virusshare download finished"

def db_refine():
    if os._exists("refine"):
        pass
    else:
        os.makedirs("refine")


def check_md5():
    db = MySQLdb.connect(host='localhost', db='pd_update', user='root', passwd='polydata', port=3306,
                         charset='utf8')
    cursor = db.cursor()
    try:
        version=time.strftime('%Y%m%d', time.localtime(time.time()))

        select_sql='select md5 from MD5 into outfile "/var/lib/mysql-files/md5_all_%s"' % version
        print select_sql
        exit()
        cursor.execute(select_sql)
        md5s = cursor.fetchall()
        cursor.close()
        db.close()
        list_md5s = [list_md5[0] for list_md5 in md5s]
    except Exception as e:
        print e
    try:
        insert_md5='insert into MD5 VALUES '

if __name__=="__main__":
     check_md5()

