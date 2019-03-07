### shell process

- all statements in the shell can be understood as processes
- in all cases where it does not feel like it is executing in the normal order, consider that the child process is not synchronized with the main process,i.e., try to use shell cmd `wait`, refer to 1.sh

#### Description of the test scripts in the current directory
1. `1.sh` denotes using the `dd` command to generate IOs.
2. `2.sh` fixes `1.sh` and increase some post-processings, e.g., blkparse,btt,etc.
3. merge.py denotes the separate read and write trace parsed by blkparse is merged into a single completed trace
4. check whether all the lsn and size fit 4K alignment