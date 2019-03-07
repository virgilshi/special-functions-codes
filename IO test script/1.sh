#! /bin/bash
blktrace
i=0
while [ $i -lt 100 ]
do
	dd if=/dev/zero of=tmp bs=8k count=1000
done
exit 0
