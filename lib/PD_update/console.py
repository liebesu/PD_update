#coding=UTF-8
from datetime import datetime,date
from lib.PD_update.packed import packed
def make_pack():
    week=datetime.now().weekday()
    print "make_pack"
    if week==4:
        update_file=packed('md5','full')
    else:
        update_file=packed('md5','increment')
    return update_file