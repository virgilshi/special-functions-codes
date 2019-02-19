#!/bin/bash

count=0
until [  "$count" == "65536" ]
do
	rand=$RANDOM
	let "rand %= 16"
	dd if=/dev/zero of="tmp${rand}" bs=8K count=1 oflag=append conv=notrunc oflag=dsync
	let "count += 1"
	
done

exit 0
