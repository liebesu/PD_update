import os
from lib.common.constants import PD_UPDATE_ROOT,PACKED_ROOT
def push_packed(update_file):
    os.system('scp %s root@192.168.25.20:/root/PolyUpgrade/Temp/ '%(update_file))
    os.chdir(PD_UPDATE_ROOT)
    os.system('python call_server.py %s'%(os.path.basename(update_file)))