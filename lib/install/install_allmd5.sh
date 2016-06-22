virusshare_path=/polydata/content/malware/md5/VirusShare/
cp md5/*.* /polydata/content/malware/md5/VirusShare/
cd /polydata/content/malware/md5/VirusShare/
rm -f *.filepart 
/polyhawk/bin/ti_mgmt_server --start
cd /polyfalcon/analysis/utils/pdmalware/bin/
if [ "`ls -A $virusshare_path `"  = "" ];then
mkdir -p /polydata/content/malware/md5/VirusShare/
/polyhawk/bin/ti_mgmt_server --compile-md5 /polydata/content/malware/md5/VirusShare/
else
/polyhawk/bin/ti_mgmt_server --compile-md5 /polydata/content/malware/md5/VirusShare/
fi
/polyhawk/bin/ti_mgmt_server --stop
/polyhawk/bin/ti_mgmt_server --start
echo "success"'