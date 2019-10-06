#! /bin/bash

set -ex

testdir=$(readlink -f $(dirname $0))
parallel=1

cd $testdir/spdk

if  test ! -e $testdir/spdk/mk/config.mk ;then
	git submodule update --init
	$testdir/spdk/scripts/pkgdep.sh
fi

./configure --enable-debug
make clean
./configure --enable-debug
make

cd $testdir/rocksdb

make clean SPDK_DIR=$testdir/spdk
make -j$parallel db_bench SPDK_DIR=$testdir/spdk

cd $testdir/spdk

if test ! -e /usr/local/etc/spdk;then
	mkdir -p /usr/local/etc/spdk
fi

scripts/gen_nvme.sh > /usr/local/etc/spdk/rocksdb.conf

HUGEMEM=5120 scripts/setup.sh

test/blobfs/mkfs/mkfs /usr/local/etc/spdk/rocksdb.conf Nvme0n1


