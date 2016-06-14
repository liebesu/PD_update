#coding:UTF-8
import MySQLdb
import os
import re
import urllib
import shutil
import time
import logging
from bs4 import BeautifulSoup
import requests
from urlparse import urljoin
__author__ = 'liebesu'

global virusshare_MD5_path
global malshare_MD5_file
global watcherlab_MD5_file

original_path='original'
log_file=os.path.join(os.getcwd(),'log','update_md5.log')
if os.path.exists(log_file):
    pass
else:
    os.makedirs(os.path.dirname(log_file))


def init_logging(debug=False):
    """日志配置"""
    log_format = '%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d : %(message)s'
    logging.basicConfig(filename=log_file, level=logging.INFO if not debug else logging.DEBUG,
                        format=log_format)
def malshare():
    '''malshare下载MD5'''
    url='http://malshare.com/daily/'
    try:
        r=requests.get(url)
    except:
        url='http://208.110.93.122/daily/'
        r=requests.get(url)
    s=BeautifulSoup(r.text,"html.parser")
    for link in s.find_all(href=re.compile('\d')):
        Dir_file=os.path.join(original_path,"malshare")
        datapath=os.path.join(Dir_file,link.get('href'))
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
                logging.info("downloading %s"% str(relurl))
                urllib.urlretrieve(relurl,os.path.join(filepath,link.get('href')))
    print "Malshare download finished"
    malshare_MD5_file=os.path.join(Dir_file,'malsahre.md5')
    os.system('find . -name "malshare_fileList.*.txt" ! -name "*sha1*" ! -name "*all*" |xargs -i cat {} >%s' % malshare_MD5_file )
def virusshare():
    '''virusshare下载MD5'''
    url='http://virusshare.com/hashes/'
    r=requests.get(url)
    s=BeautifulSoup(r.content,"html.parser")
    links=s.find_all(href=re.compile('^VirusShare'))
    virusshare_path=os.path.join(original_path,"virusshare")
    if os.path.exists(virusshare_path):
        pass
    else:
        os.makedirs(virusshare_path)

    for link in links:
        filepath = os.path.join(virusshare_path, link.get('href'))
        realurl=urljoin(url,link.get('href'))
        if os.path.exists(filepath):
            pass
        else:
            logging.info("virusshare downloading %s" % str(realurl))
            urllib.urlretrieve(realurl,filepath)
    print "virusshare download finished"
    virusshare_MD5_path=os.path.join(virusshare_path,'virusshare.md5')
    os.system('find . -name "VirusShare_*.md5" |xargs -i cat {} >%s' % virusshare_MD5_path )
def watchlab_feed():
    '''守望者实验室feed'''
    url = 'http://feed.watcherlab.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tgzs = soup.find_all(href=re.compile("watcherlab-\d"))  
    for tgz in tgzs:
        tgzurl = urljoin(url, tgz.get('href'))
        watcherlab_path=os.path.join(original_path,"watcherlab")
        watcherlab_untaz_path=os.path.join(watcherlab_path,"watcherlab_untaz")
        if os.path.exists(watcherlab_untaz_path):
            pass
        else:
            os.makedirs(watcherlab_untaz_path)          
        if os.path.exists(watcherlab_path):
            pass
        else:
            os.makedirs(watcherlab_path)
        if os.path.exists(os.path.join(watcherlab_path, os.path.basename(tgzurl))):
            pass
        else:
            tgz_path = os.path.join(watcherlab_path, os.path.basename(tgzurl))
            logging.info("watchlab downloading %s" % str(tgzurl))
            urllib.urlretrieve(tgzurl, tgz_path)
        
            os.system("tar zxvf " + tgz_path + " -C %s " % watcherlab_untaz_path)
    print "watcherlab download finished"
    watcherlab_MD5_file=os.path.join(watcherlab_path,'watcherlab_blackmd5.md5')
    os.system('find . -name "watcherlab-md5*" | xargs -i cut -f 2 -d "," {}  >%s' % watcherlab_MD5_file)


def db_refine():
    '''数据清洗'''
    print "111"
    refine_path=os.path.join(os.getcwd(),"refine")
    if os._exists(refine_path):
        shutil.rmtree(refine_path)
        os.makedirs(refine_path)
    else:
        os.makedirs(refine_path)
    shutil.copyfile(virusshare_MD5_path, refine_path)
    shutil.copyfile(malshare_MD5_file, refine_path)
    shutil.copyfile(watcherlab_MD5_file, refine_path)
    logging.info('copy %s %s %s'%(virusshare_MD5_path,malshare_MD5_file,watcherlab_MD5_file))

def check_md5():
    '''数据库检查更新'''
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
    
    insert_md5='insert into MD5 VALUES '
   
    

if __name__ =="__main__":
    init_logging(debug=True)
    malshare()
    virusshare()
    watchlab_feed()
    db_refine()

