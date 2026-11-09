from datetime import datetime
import os

# Get current date and time in YYYY/mm/dd hh:mm:ss format
now = datetime.now()
timestamp = now.strftime("%Y/%m/%d %H:%M:%S")

log_message = f"Python script execution timestamp: {timestamp}\n"

print(log_message)

# Optional: If you want to append this to a log file inside the repo (or just print it)
with open("execution.log", "a") as log_file:
    log_file.write(log_message)