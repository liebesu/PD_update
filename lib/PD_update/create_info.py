#coding:UTF-8
import os
import json
import time
from lib.common.constants import PD_UPDATE_ROOT
def create_info_file(target):
    if target=='AVEngineDB':
        ID="3001"
        chtarget="反病毒引擎特征码"
        suffix="sh"
        type="shell"
        IsVisible="1" 
    elif target== "SandboxSignatures" :
        ID="3002"
        chtarget="动态行为检测规则"
        suffix="py"
        type="python"
        IsVisible="1"
    elif target== "YaraRules" :
        ID="3003"
        chtarget="Yara规则"
        suffix="sh"
        type="shell"
        IsVisible="1"
    elif target== "JsunpackRules" :
        ID="3004"
        chtarget="CVE漏洞特征"
        suffix="sh"
        type="shell"
        IsVisible="1"
    elif target== "ReputationData" :
        ID="3005"
        chtarget="威胁情报数据"
        suffix="sh"
        type="shell"
        IsVisible="1"
    elif target== "MD5Data" :
        ID="3007"
        chtarget="哈希校验数据"
        suffix="sh"
        type="shell"
        IsVisible="1"
    elif target== "PEiDRules" :
        ID="3008"
        chtarget="PEiD规则"
        suffix="sh"
        type="shell"
        IsVisible="1"
    elif target== "GeographicalLocationInfo" :
        ID="3006"
        chtarget="地理位置信息"
        suffix="sh"
        type="shell"
        IsVisible="0"
    
    
    version=time.strftime('%Y%m%d', time.localtime(time.time()))
    yest_version=time.strftime('%Y%m%d', time.localtime(time.time()-24*60*60))
    content='{"ProductId": '+ID+',"ProductName": {"en":"'+target+'","ch": "'+chtarget+'","ProductType": "Client","ProductInfo": {"langCode": "CN_ZH","OEM": "","description": ""},"PlatformInfo": {"os": "Linux","vender": "Ubuntu","architecture": "X86","version": "14.04"},"IsVisible": '+IsVisible+',"UpdatePaths": {"from": {"minimum": "1.0.0.20151202","maximum": "1.0.0.'+yest_version+'"},"to": "1.0.0.'+version+'","required": []},"InstallInfo": {"version": "1.0.0.'+version+'","path": "install.'+suffix+'","type": "'+type+'"}}}'
    info_json_path=os.path.join(PD_UPDATE_ROOT,"lib","install","info.json")
    a=open(info_json_path,"w")
    a.write(content)
    a.close
