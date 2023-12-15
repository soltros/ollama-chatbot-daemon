import subprocess
import time

# Run npm run dev in the background and disconnect from the terminal
proc = subprocess.Popen(['npm', 'run', 'dev'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
disown

# Get the process ID of the running process
pid = proc.pid

# Wait for a key press to terminate the program
input("Press enter to stop the program: ")

# Terminate the program using the process ID
proc.kill()
