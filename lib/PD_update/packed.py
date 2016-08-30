import os
import zipfile
import shutil
import time
from lib.common.constants import PD_UPDATE_ROOT,TMP_ROOT
def create_json():
    json_path=os.path.normpath(os.path.join(PD_UPDATE_ROOT,"lib","install","info_model.json"))
    a=open(json_path)
def packed(Category,mode):
    packed_path=os.path.normpath(os.path.join(PD_UPDATE_ROOT,"packed"))
    if os.path.exists(packed_path):
        pass
    else:
        os.makedirs(packed_path)
    if Category=='md5':
        global version
        version=time.strftime('%Y%m%d', time.localtime(time.time()))        
        tmp_md5_path=os.path.normpath(os.path.join(TMP_ROOT,"MD5"))
        tmp_md5_version_path=os.path.normpath(os.path.join(tmp_md5_path,"MD5Data_1.0.0.{}".format(version)))
        tmp_md5_version_filepath=os.path.join(tmp_md5_version_path,"md5")
        if os.path.exists(tmp_md5_version_filepath):
            pass
        else:
            os.makedirs(tmp_md5_version_filepath)
        
        if mode=='increment':
            shutil.copyfile(os.path.join(PD_UPDATE_ROOT,"lib","install","install_newmd5.sh"), os.path.join(tmp_md5_version_path,"install.sh"))
            shutil.copyfile(os.path.join(PD_UPDATE_ROOT,"lib","install","info.json"),os.path.join(tmp_md5_version_path,"info.json"))
            shutil.copyfile(os.path.join(PD_UPDATE_ROOT,"data","md5","result","new_{}.MD5".format(version)),os.path.join(tmp_md5_version_filepath,"new_{}.MD5".format(version)))
            os.chdir(tmp_md5_path)        
            os.system("zip -r %s/MD5Data_1.0.0.%s.zip MD5Data_1.0.0.%s"%(tmp_md5_path,version,version))
            shutil.copy('%s/MD5Data_1.0.0.%s.zip'%(tmp_md5_path,version), packed_path)
            os.system("rm -r %s"%(tmp_md5_path))
            md5_update_file=os.path.normpath(os.path.join(packed_path,"MD5Data_1.0.0.%s.zip"%(version)))                
        elif mode=='full':
            shutil.copyfile(os.path.join(PD_UPDATE_ROOT,"lib","install","install_allmd5.sh"), os.path.join(tmp_md5_version_path,"install.sh"))
            shutil.copyfile(os.path.join(PD_UPDATE_ROOT,"lib","install","info.json"),os.path.join(tmp_md5_version_path,"info.json"))
            shutil.copyfile(os.path.join(PD_UPDATE_ROOT,"data","md5","result","db_md5_all_{}.md5".format(version)),os.path.join(tmp_md5_version_filepath,"db_md5_all_{}.md5".format(version)))
            os.chdir(tmp_md5_path)        
            os.system("zip -r %s/MD5Data_1.0.0.%s_full.zip MD5Data_1.0.0.%s"%(tmp_md5_path,version,version))
            shutil.copy('%s/MD5Data_1.0.0.%s_full.zip'%(tmp_md5_path,version), packed_path)
            os.system("rm -r %s"%(tmp_md5_path))
            md5_update_file=os.path.normpath(os.path.join(packed_path,"MD5Data_1.0.0.%s_full.zip"%(version)))    
    return md5_update_file