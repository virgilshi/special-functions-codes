#! /bin/bash
blktrace -d /dev/sdb -o trace.out
i=0
while [ $i -lt 100 ]
do
	dd if=/dev/zero of=/dev/sdb  bs=8k count=1000
done
exit 0
