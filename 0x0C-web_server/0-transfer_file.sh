#!/usr/bin/env bash
# a script that copies a file to a remote server
# accepts four arguments

if [$# -lt 4]; then
    echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
else
    scp -o StrictHostKeyChecking=no -i $4 $1 $2 $3
fi
