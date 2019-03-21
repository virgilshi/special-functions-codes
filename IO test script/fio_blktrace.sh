#!/bin/bash
# run: . sh
cd /home/f2fs/trace/
blktrace -d /dev/sdb -o qq &
cd /mnt/f2fs
fio -f fio-rand-RW.fio 
kill -9 `ps -aux | grep blktrace | awk '{if (NR==1) print $2}'`
wait
cd /home/f2fs/trace/
blkparse -i qq -d qq.out
btt -i qq.out -B qq.off

