#coding=UTF-8
from datetime import datetime,date
from lib.PD_update.packed import packed
from lib.PD_update.create_info import create_info_file
from lib.PD_update.push import push_packed
def make_pack():
    week=datetime.now().weekday()
    print "make_pack"
    if week==4:
        #周五增量和全量
        #先增量
        create_info_file('MD5Data',"increment")
        update_file=packed('md5','increment')
        push_packed(update_file)
        print "push packed",update_file
        #后全量
        create_info_file('MD5Data','full')
        update_file=packed('md5','full')
        push_packed(update_file)
        print "push packed",update_file        
    else:
        #除了周五 增量
        create_info_file('MD5Data',"increment")
        update_file=packed('md5','increment')
        push_packed(update_file)
        print "push packed",update_file
    