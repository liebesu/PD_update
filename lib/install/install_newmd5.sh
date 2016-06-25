#!/bin/bash
virusshare_path=/polydata/content/malware/md5/VirusShare/
Cur_Dir=$(pwd)

ti_mgmt_server --start

if [ "`ls -A $virusshare_path `"  = "" ];then
mkdir -p /polydata/content/malware/md5/VirusShare/
ti_mgmt_client --add-md5 $Cur_Dir/md5/*.MD5
else
ti_mgmt_client --add-md5 $Cur_Dir/md5/*.MD5
fi
cd /polydata/content/malware/md5/VirusShare/
rm -f *.filepart 
ti_mgmt_server --stop
ti_mgmt_server --start
