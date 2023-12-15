#!/usr/bin/env python3

import subprocess
import time

# Run npm run dev in the background
proc = subprocess.Popen(['npm', 'run', 'dev'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Get the process ID of the running process (optional, as it's not used here)
pid = proc.pid

# Wait for a key press to terminate the program
input("Press enter to stop the program: ")

# Terminate the program using the process ID
proc.kill()
proc.wait()  # Wait for process to terminate completely
