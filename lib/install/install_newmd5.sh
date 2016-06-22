virusshare_path=/polydata/content/malware/md5/VirusShare/


/polyhawk/bin/ti_mgmt_server --start
cd /polyfalcon/analysis/utils/pdmalware/bin/
if [ "`ls -A $virusshare_path `"  = "" ];then
mkdir -p /polydata/content/malware/md5/VirusShare/
/polyhawk/bin/ti_mgmt_client --add-md5 md5/*.md5
else
/polyhawk/bin/ti_mgmt_server --add-md5 md5/*.md5
fi
cd /polydata/content/malware/md5/VirusShare/
rm -f *.filepart 
/polyhawk/bin/ti_mgmt_server --stop
/polyhawk/bin/ti_mgmt_server --start
echo "success"'