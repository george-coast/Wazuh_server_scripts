import os
import subprocess
from datetime import datetime, timedelta

# change to the dir
os.chdir('/var/ossec/logs/archives')

# Get the current time
now = datetime.now()

# If it's within the first hour of the day, use the previous day
if now.hour < 1:
    target_date = now - timedelta(days=1)
else:
    target_date = now

# Format the date as 'MM-DD'
date_str = target_date.strftime('%m-%d')

# Construct the command
command = f'/usr/local/bin/linode-cli obj put archives.log new5571/{date_str}'

# Execute the command
subprocess.run(command, shell=True)
