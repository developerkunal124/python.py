from datetime import datetime

current_time = datetime.now()

hours = current_time.hour
minute = current_time.minute
second = current_time.second

print(f"the time is:{hours:02d}:{minute:02d}:{second:02d}")