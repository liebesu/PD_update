#!/bin/bash
virusshare_path=/polydata/content/malware/md5/VirusShare/
cp md5/*.* /polydata/content/malware/md5/VirusShare/
cd /polydata/content/malware/md5/VirusShare/
rm -f *.filepart
rm -f *.md5.1
ti_mgmt_server --start

if [ "`ls -A $virusshare_path `"  = "" ];then
mkdir -p /polydata/content/malware/md5/VirusShare/
ti_mgmt_server --compile-md5 /polydata/content/malware/md5/VirusShare/
else
ti_mgmt_server --compile-md5 /polydata/content/malware/md5/VirusShare/
fi
ti_mgmt_server --stop
ti_mgmt_server --start
