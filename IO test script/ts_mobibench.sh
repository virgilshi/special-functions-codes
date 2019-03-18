# /bin/bash
echo  "replay times: $1"

cnt=0
while [ $cnt -lt $1 ]
do
    echo  "start replay: $cnt" | tee -a result.log
    date | tee -a result.log
    mobibench -p /mnt/f2fs  -g $2 | tee -a result.log
    let cnt++
    sync; echo 3 > /proc/sys/vm/drop_caches
    ls /mnt/f2fs && rm -rf /mnt/f2fs/mobigen_temp && ls /mnt/f2fs
    
done 
exit 0