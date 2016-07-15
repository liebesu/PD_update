import argparse
from multiprocessing.pool import Pool
import os
import urllib
import requests
import MySQLdb
downloader_path='malshare'
__author__ = 'liebesu'
def downloader(hash_md5):
    apikey='a6761270a4edb516387196309b80ea6df3ca58af32335aa8283a9fd8ee587b9d'
    payload={'action':'getfile','api_key':apikey,'hash':hash_md5}
    url='http://malshare.com/sampleshare.php'
    r=requests.post(url,params=payload)
    if os.path.exists(downloader_path):
        urllib.urlretrieve(r.url,hash_md5)
        print "downloading..."
    else:
        os.makedirs(downloader_path)
        urllib.urlretrieve(r.url,hash_md5)
        print "downloading..."
def get_hash(num):
    db=MySQLdb.connect(host='localhost',db='virusname',user='root',passwd='polydata',port=3306,charset='utf8')
    cursor=db.cursor()
    try:
        select_sql='select MD5 from malshare ORDER BY rand() limit 0,%d'%(num)
        cursor.execute(select_sql)
        md5s=cursor.fetchall()
        cursor.close()
        db.close()
        list_md5s=[list_md5[0] for list_md5 in md5s]
        pool(list_md5s)
    except Exception as e:
        print e

def pool(md5s):
    pool=Pool(processes=10)
    pool.map(downloader,md5s)
    pool.close()
    pool.join()
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n",type=int,help="downloader virus numbers")
    args = parser.parse_args()
    num=args.n
    get_hash(num)
    print "downloader finihed ",num
