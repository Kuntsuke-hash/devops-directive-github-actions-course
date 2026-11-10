from datetime import datetime, timezone

print("UTC:", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
print("Local:", datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"))