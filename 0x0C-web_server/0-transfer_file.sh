#!/usr/bin/env bash
# a script that copies a file to a remote server
# accepts four arguments

file_path = $1
IP = $2
user_name = $3
path_to_ssh_key = $4
detination = ~/

if [$# -lt 4]; then
    echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
else
    scp -o StrictHostKeyChecking=no -i "$path_to_ssh_key" "$file_path" "$user_name@$IP:$destination"
fi
