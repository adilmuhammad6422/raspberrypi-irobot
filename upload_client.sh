#!/bin/bash
# sudo apt-get install sshpass <-- to install sshpass

# List of device IP addresses
DEVICES=("192.168.1.180" "192.168.1.168" "192.168.1.158" "192.168.1.197" "192.168.1.171" "192.168.1.167" "192.168.1.169" "192.168.1.155" "192.168.1.196")  # Replace with your actual IPs

# File to upload
FILE="client"

# Credentials
USER="pi"
PASS="raspberry"

# Loop through each device and upload the file
for IP in "${DEVICES[@]}"; do
    echo "Uploading to $IP..."
    sshpass -p "$PASS" sftp -o StrictHostKeyChecking=no "$USER@$IP" <<EOF
    put $FILE
    EOF
done
