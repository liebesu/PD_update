import ConfigParser,os
from constants import  PD_UPDATE_ROOT
def read_conf():
    conf_path=os.path.normpath(os.path.join(PD_UPDATE_ROOT,"conf","conf.cnf"))
    config=ConfigParser.ConfigParser()
    config.read(conf_path)
    initial_time=config.get("initial time", "initial_time")
    return initial_time