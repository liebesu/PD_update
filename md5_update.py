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
    global malshare_MD5_file
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
    global virusshare_MD5_path
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
    global watcherlab_MD5_file
    watcherlab_MD5_file=os.path.join(watcherlab_path,'watcherlab_blackmd5.md5')
    os.system('find . -name "watcherlab-md5*" | xargs -i cut -f 2 -d "," {}  >%s' % watcherlab_MD5_file)

def other_md5():
    
    global other_md5_file
    dir_other=os.path.join(original_path,'other')
    other_md5_file=os.path.join(dir_other,'all_other.md5')
    os.system('find %s -name "*.md5" ! -name "all_other.md5" | xargs -i cat {} >%s'% (dir_other,other_md5_file) )
def db_refine():
    '''数据清洗'''
    refine_path=os.path.join(os.getcwd(),"refine")
    if os.path.exists(refine_path):
        shutil.rmtree(refine_path)
        os.makedirs(refine_path)
    else:
        os.makedirs(refine_path)
    
    os.system("sed -i '/#/d' %s"%(malshare_MD5_file))
    logging.info("sed  '/#/d' %s"%(malshare_MD5_file))
    os.system("sed  -i '/#/d' %s"%(virusshare_MD5_path))
    logging.info("sed -i '/#/d' %s"%(watcherlab_MD5_file))    
    shutil.copy(virusshare_MD5_path, refine_path)
    logging.info('copy %s'% virusshare_MD5_path)
    shutil.copy(malshare_MD5_file, refine_path)
    logging.info('copy %s'% malshare_MD5_file)
    shutil.copy(watcherlab_MD5_file, refine_path)
    logging.info('copy %s '% watcherlab_MD5_file)
    shutil.copy(other_md5_file, refine_path)
    logging.info('copy %s' % other_md5_file)
    
    global result_path
    result_path=os.path.join(os.getcwd(),'result')
    if os.path.exists(result_path):
        pass
    else:
        os.makedirs(result_path)
    os.system('cat %s/*.md5 |uniq  >%s/md5_refine_result.md5'%(refine_path,result_path))
    logging.info('create %s/md5_refine_result.md5'%(result_path))
    global md5_refine_result
    md5_refine_result=os.path.join(result_path,'md5_refine_result.md5')
def check_md5():
    '''数据库检查更新'''
    logging.info('use mysqldb')
    db = MySQLdb.connect(host='localhost', db='pd_update', user='root', passwd='polydata', port=3306,
                         charset='utf8')
    cursor = db.cursor()
    try:
        select_sql='select md5 from MD5 into outfile "/var/lib/mysql-files/db_md5_all_%s.md5"' % version
        cursor.execute(select_sql)  
        cursor.close()
        db.close()
    except Exception as e:
        print e
    logging.info("mysql outfile /var/lib/mysql-files/db_md5_all_%s.md5"% version)
    os.system('cp /var/lib/mysql-files/db_md5_all_%s.md5 %s'% (version,result_path))
    logging.info('cp /var/lib/mysql-files/db_md5_all_%s.md5 %s'% (version,result_path))
    os.system('rm /var/lib/mysql-files/db_md5_all_%s.md5'% version)
    logging.info('rm /var/lib/mysql-files/db_md5_all_%s.md5'% version)
    os.system('cat %s/db_md5_all_%s.md5 %s  | uniq -u >%s/new_%s'%(result_path,version,md5_refine_result,result_path,version))
    logging.info('cat %s/db_md5_all_%s.md5 %s  | uniq -u >%s/new_%s'%(result_path,version,md5_refine_result,result_path,version))
    exit()
    insert_md5='insert into MD5 VALUES '
   
    

if __name__ =="__main__":
    init_logging(debug=True)
    version=time.strftime('%Y%m%d', time.localtime(time.time()))
    malshare()
    virusshare()
    watchlab_feed()
    other_md5()
    db_refine()
    check_md5()
