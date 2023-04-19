#!/bin/bash

# Create the /root/keys directory if it doesn't exist
if [ ! -d "/root/keys" ]; then
    mkdir /root/keys
fi

# Copy the zencrypt.py script to /root/keys
cp zencrypt.py /root/keys/zencrypt.py
chmod +x /root/keys/zencrypt.py

# Copy the zencrypt shell script to /sbin
cp zencrypt /sbin/zencrypt
chmod +x /sbin/zencrypt

echo "Installation completed. You can now use the 'zencrypt' command."
