#! /bin/bash

set -ex

cd /root/sl/spdk

make clean
./configure --enable-debug
make

cd /root/sl/spdk_rocksdb/rocksdb

make clean SPDK_DIR=/root/sl/spdk
make db_bench SPDK_DIR=/root/sl/spdk

cd /root/sl/spdk

scripts/gen_nvme.sh > /usr/local/etc/spdk/rocksdb.conf

HUGEMEM=5120 scripts/setup.sh

test/blobfs/mkfs/mkfs /usr/local/etc/spdk/rocksdb.conf Nvme0n1


