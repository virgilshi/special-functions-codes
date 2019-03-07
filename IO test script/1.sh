#! /bin/bash
blktrace -d /dev/sdb -o trace.out &
i=0
while [ $i -lt 10 ]
do
	dd if=/dev/zero of=/dev/sdb  bs=8k count=1000
	let i++
done
kill -2 `ps -aux | grep blktrace | head -n1 | awk '{print $2}'`
echo "end1"
wait
blktrace -d /dev/sdb -o trace.out &
i=0
while [ $i -lt 10 ]
do
	dd if=/dev/zero of=/dev/sdb  bs=8k count=1000
	let i++
done
kill -2 `ps -aux | grep blktrace | head -n1 | awk '{print $2}'`
wait # block shell process,waiting all the subprocess generated by it to run to here, i.e., synchronous
echo "end2"
exit 0