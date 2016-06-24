import os
from lib.common.constants import PD_UPDATE_ROOT,DATA_ROOT,TMP_ROOT

def make_new_floder():
    if os.path.exists(DATA_ROOT):
        pass
    else:
        os.makedirs(DATA_ROOT)
    if os.path.exists(TMP_ROOT):
        pass
    else:
        os.makedirs(TMP_ROOT)
    